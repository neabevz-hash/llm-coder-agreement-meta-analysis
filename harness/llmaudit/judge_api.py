"""LLM judges through the OpenRouter API.

Same codebook prompt and JSON schema as the Claude judge. Two ways to constrain
the output:
  * schema_mode="strict": the provider's structured output (json_schema, strict);
  * schema_mode="json_object": JSON mode for providers without structured output;
    the schema is then appended to the system message.
Every reply is validated against the schema here; invalid replies are retried.

The grief-bots pilot used temperature 0 and max_tokens 4000 (the defaults below).
The judge-validation study passes temperature=None (provider default) and its own cap.
"""

from __future__ import annotations

import asyncio
import copy
import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import jsonschema

from .env import git_version, require
from .openrouter import CallError, OpenRouter


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def strict_schema(schema: dict) -> dict:
    """Strict structured-output mode rejects some keywords (e.g. maxLength, $schema)."""
    s = copy.deepcopy(schema)

    def walk(node):
        if isinstance(node, dict):
            for k in ("maxLength", "minLength", "$schema", "title"):
                node.pop(k, None)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(s)
    return s


def system_with_schema(system_prompt: str, schema: dict) -> str:
    """System message for JSON mode: the prompt plus the schema the reply must satisfy."""
    return (system_prompt + "\n\nThe JSON object must validate against this JSON Schema:\n"
            + json.dumps(strict_schema(schema), separators=(",", ":")))


def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


async def judge_all_api(items: list[dict], render: Callable[[dict], str], *, system_prompt: str,
                        schema: dict, model: str, out: Path, provider: dict | None = None,
                        concurrency: int = 6, seed: int = 20261004, limit: int | None = None,
                        max_attempts: int = 3, temperature: float | None = 0.0,
                        max_tokens: int = 4000, schema_mode: str = "strict",
                        reasoning: dict | None = None, label: str | None = None) -> dict:
    """Judge every item not yet in `out`; one JSON line per item. Returns run stats."""
    validator = jsonschema.Draft202012Validator(schema)
    done = set()
    if out.exists():
        with out.open(encoding="utf-8") as f:
            done = {json.loads(line)["conv_id"] for line in f if line.strip()}
    todo = [it for it in items if it["conv_id"] not in done]
    random.Random(seed).shuffle(todo)
    if limit is not None:
        todo = todo[:limit]
    name = label or model
    print(f"[judge-api] {name}: {len(items)} items, {len(done)} done, {len(todo)} to judge", flush=True)
    stats = {"ok": 0, "fail": 0, "usd": 0.0, "usd_failed_attempts": 0.0}
    if not todo:
        return stats
    out.parent.mkdir(parents=True, exist_ok=True)
    errors_path = out.with_suffix(out.suffix + ".errors.jsonl")
    if schema_mode == "strict":
        system = system_prompt
        fmt = {"type": "json_schema",
               "json_schema": {"name": "codes", "strict": True, "schema": strict_schema(schema)}}
    elif schema_mode == "json_object":
        system = system_with_schema(system_prompt, schema)
        fmt = {"type": "json_object"}
    else:
        raise ValueError(f"unknown schema_mode {schema_mode!r}")
    extra: dict = {"response_format": fmt}
    if temperature is not None:
        extra["temperature"] = temperature
    fingerprint = {"model_requested": model, "provider_requested": provider,
                   "temperature": temperature, "max_tokens": max_tokens,
                   "schema_mode": schema_mode, "reasoning": reasoning,
                   "system_prompt_sha": sha(system),
                   "schema_sha": sha(json.dumps(schema, sort_keys=True)),
                   "harness": git_version()}
    sem, lock = asyncio.Semaphore(concurrency), asyncio.Lock()

    async with OpenRouter(require("OPENROUTER_API_KEY")) as client:
        async def worker(item: dict) -> None:
            async with sem:
                prompt = render(item)
                last, spent, calls = None, 0.0, []
                for attempt in range(1, max_attempts + 1):
                    res = None
                    try:
                        res = await client.chat(
                            model, [{"role": "system", "content": system},
                                    {"role": "user", "content": prompt}],
                            provider=provider, reasoning=reasoning, max_tokens=max_tokens,
                            extra=extra)
                        spent += res.usage.get("cost") or 0.0
                        calls.append(res.meta())
                        if res.blocked:
                            raise ValueError(f"blocked (finish={res.finish_reason})")
                        codes = parse_json(res.content)
                        errs = list(validator.iter_errors(codes))
                        if errs:
                            raise ValueError("schema: " + "; ".join(e.message for e in errs[:3]))
                        rec = {"conv_id": item["conv_id"], "judged_at": utcnow(),
                               "judge": fingerprint | {"model": res.model, "provider": res.provider},
                               "prompt_sha": sha(prompt), "codes": codes, "attempts": attempt,
                               "duration_s": round(sum(c["latency_s"] for c in calls), 1),
                               "usage": res.usage, "usd": round(spent, 6),
                               "finish_reason": res.finish_reason,
                               "reasoning_chars": len(res.reasoning or "")}
                        async with lock:
                            stats["ok"] += 1
                            stats["usd"] += spent
                            with out.open("a", encoding="utf-8", newline="\n") as f:
                                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                        print(f"[judge-api ok {stats['ok']}/{len(todo)}] {name} {item['conv_id']} "
                              f"${stats['usd']:.3f}", flush=True)
                        return
                    except (CallError, ValueError, json.JSONDecodeError) as e:
                        last = e
                        if res is None and isinstance(e, CallError):
                            calls.append({"error": str(e)[:300]})
                        await asyncio.sleep(3 * attempt)
                async with lock:
                    stats["fail"] += 1
                    stats["usd_failed_attempts"] += spent
                    with errors_path.open("a", encoding="utf-8", newline="\n") as f:
                        f.write(json.dumps({"conv_id": item["conv_id"], "at": utcnow(),
                                            "error": str(last)[:500], "usd": round(spent, 6),
                                            "calls": calls}, ensure_ascii=False) + "\n")
                print(f"[judge-api fail] {name} {item['conv_id']}: {str(last)[:200]}", flush=True)

        await asyncio.gather(*(worker(it) for it in todo))
    print(f"[judge-api] {name} finished: {stats['ok']} ok, {stats['fail']} failed, "
          f"${stats['usd']:.3f} (+${stats['usd_failed_attempts']:.3f} in failed items)", flush=True)
    return stats
