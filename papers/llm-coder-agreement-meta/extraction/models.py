"""Model attributes for G3 and the moderators (codebook `release_date`, `reasoning_model`, `open_weights`; D7).

Each estimate's model name (as reported) is mapped to one model by the ordered rules below (first match wins).
Release dates: the developer's announcement for models released before 2025, and for later models the date the model
was listed in the OpenRouter catalogue (https://openrouter.ai/api/v1/models, read 2026-10-23), which follows the
announcement within days; a snapshot date in the model ID wins over both. Ensembles, pooled values, unnamed models and
products whose underlying model is not stated get no date and drop out of the G3 analyses only.
Generations (protocol §15b): to 2023-03; GPT-4 era to 2024-04; GPT-4o era to 2024-12; 2025-2026.

Writes forms/model_releases.csv (one row per model) and annotates the estimate rows (finalize.py calls annotate()).
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

FORMS = Path(__file__).resolve().parent.parent / "forms"
D, OR, S = "developer announcement", "OpenRouter listing", "snapshot in model ID"

# (pattern on the lower-cased name, model, developer, release, source, reasoning, open weights)
RULES = [
    (r"ensemble|pooled|aggregate|average of|averaged|majority vote|jury|consensus of|union of|aisilver|\s\+\s|"
     r"\b\d+ llms?\b|all 8|unnamed|unspecified|not named|model not|llm evaluator|weighted ensemble|final five-judge|"
     r"rag \+ llm|dawid|mace|ordinal ds|^\d+ llm", None, "", "", "", "", ""),
    (r"notebooklm|qualigpt|^muse$|themis|^jev-|ocsai|m-prometheus|doubao universal|gigachat|^mimo$|minicpm|"
     r"granite4|hy4|claude sonnet \(extended|^chatgpt$|^llama$|^llama-70b$", None, "", "", "", "", ""),
    (r"flan-t5", "Flan-T5-Large", "Google", "2022-10-20", D, "no", "yes"),
    (r"text-davinci-002|^gpt-3 ", "GPT-3 text-davinci-002", "OpenAI", "2022-03-15", D, "no", "no"),
    (r"gpt-6\.1", "GPT-6.1 Sol", "OpenAI", "2026-09-29", OR, "yes", "no"),
    (r"gpt-6", "GPT-6 Astra", "OpenAI", "2026-09-04", OR, "yes", "no"),
    (r"gpt-5\.6", "GPT-5.6", "OpenAI", "2026-07-09", OR, "yes", "no"),
    (r"gpt-5\.5|chatgpt 5\.5", "GPT-5.5", "OpenAI", "2026-04-24", OR, "yes", "no"),
    (r"gpt-5\.4.?mini", "GPT-5.4 mini", "OpenAI", "2026-03-17", OR, "yes", "no"),
    (r"gpt-5\.4", "GPT-5.4", "OpenAI", "2026-03-05", OR, "yes", "no"),
    (r"gpt-5\.3|chatgpt 5\.3", "GPT-5.3", "OpenAI", "2026-02-24", OR, "yes", "no"),
    (r"gpt-5\.2|chatgpt.5\.2", "GPT-5.2", "OpenAI", "2025-12-11", S, "yes", "no"),
    (r"gpt-5\.1", "GPT-5.1", "OpenAI", "2025-11-13", OR, "yes", "no"),
    (r"gpt-5.?nano", "GPT-5 nano", "OpenAI", "2025-08-07", D, "yes", "no"),
    (r"gpt-5-chat|gpt-5 \(gpt-5-chat", "GPT-5 Chat", "OpenAI", "2025-08-07", D, "no", "no"),
    (r"gpt-5|chatgpt-5", "GPT-5", "OpenAI", "2025-08-07", D, "yes", "no"),
    (r"gpt-oss-safeguard", "gpt-oss-safeguard-20b", "OpenAI", "2025-10-29", OR, "yes", "yes"),
    (r"gpt.oss", "gpt-oss", "OpenAI", "2025-08-05", D, "yes", "yes"),
    (r"gpt-audio-2025-08-28", "gpt-audio", "OpenAI", "2025-08-28", S, "no", "no"),
    (r"gpt-4\.5", "GPT-4.5", "OpenAI", "2025-02-27", D, "no", "no"),
    (r"gpt-4\.1", "GPT-4.1", "OpenAI", "2025-04-14", S, "no", "no"),
    (r"4o.?mini", "GPT-4o mini", "OpenAI", "2024-07-18", S, "no", "no"),
    (r"gpt-4o-2024-11-20", "GPT-4o", "OpenAI", "2024-11-20", S, "no", "no"),
    (r"2024-08-06|08-06-2024|august 2024", "GPT-4o", "OpenAI", "2024-08-06", S, "no", "no"),
    (r"gpt.?4o|chatgpt4o", "GPT-4o", "OpenAI", "2024-05-13", D, "no", "no"),
    (r"o4-mini", "o4-mini", "OpenAI", "2025-04-16", D, "yes", "no"),
    (r"o3-mini", "o3-mini", "OpenAI", "2025-01-31", S, "yes", "no"),
    (r"\bo3\b|gpt o3|gtp o3", "o3", "OpenAI", "2025-04-16", D, "yes", "no"),
    (r"o1.?pro", "o1 pro", "OpenAI", "2024-12-05", D, "yes", "no"),
    (r"o1-mini", "o1-mini", "OpenAI", "2024-09-12", S, "yes", "no"),
    (r"\bo1\b", "o1", "OpenAI", "2024-12-05", D, "yes", "no"),
    (r"gpt-4-0125", "GPT-4 Turbo (0125)", "OpenAI", "2024-01-25", S, "no", "no"),
    (r"gpt-4-1106", "GPT-4 Turbo (1106)", "OpenAI", "2023-11-06", S, "no", "no"),
    (r"gpt-4.turbo|gpt-4 \(gpt-4 turbo", "GPT-4 Turbo", "OpenAI", "2024-04-09", D, "no", "no"),
    (r"gpt-4|chatgpt-4", "GPT-4", "OpenAI", "2023-03-14", D, "no", "no"),
    (r"3\.5-turbo-0125", "GPT-3.5 Turbo (0125)", "OpenAI", "2024-01-25", S, "no", "no"),
    (r"3\.5-turbo-1106", "GPT-3.5 Turbo (1106)", "OpenAI", "2023-11-06", S, "no", "no"),
    (r"3\.5-turbo-0613|35-turbo-16k", "GPT-3.5 Turbo (0613)", "OpenAI", "2023-06-13", S, "no", "no"),
    (r"gpt-3\.5|chatgpt.3\.5|^chatgpt \(gpt-35", "GPT-3.5 Turbo", "OpenAI", "2022-11-30", D, "no", "no"),
    (r"fable 5|fable-5", "Claude Fable 5", "Anthropic", "2026-06-09", OR, "no", "no"),
    (r"opus 5\.5|opus-5-5", "Claude Opus 5.5", "Anthropic", "2026-09-22", OR, "no", "no"),
    (r"sonnet.5\.5|sonnet-5-5", "Claude Sonnet 5.5", "Anthropic", "2026-09-28", OR, "no", "no"),
    (r"sonnet.5\b|sonnet-5$", "Claude Sonnet 5", "Anthropic", "2026-06-30", OR, "no", "no"),
    (r"opus 4\.8", "Claude Opus 4.8", "Anthropic", "2026-05-27", OR, "no", "no"),
    (r"opus.4.7", "Claude Opus 4.7", "Anthropic", "2026-04-16", OR, "no", "no"),
    (r"opus 4\.6", "Claude Opus 4.6", "Anthropic", "2026-02-04", OR, "no", "no"),
    (r"sonnet.4.6", "Claude Sonnet 4.6", "Anthropic", "2026-02-17", OR, "no", "no"),
    (r"opus-4-5", "Claude Opus 4.5", "Anthropic", "2025-11-24", D, "no", "no"),
    (r"haiku.4.5", "Claude Haiku 4.5", "Anthropic", "2025-10-15", D, "no", "no"),
    (r"sonnet.4.5|4\.5-sonnet", "Claude Sonnet 4.5", "Anthropic", "2025-09-29", D, "no", "no"),
    (r"sonnet 4|claude 4 sonnet|sonnet-4-2025", "Claude Sonnet 4", "Anthropic", "2025-05-22", D, "no", "no"),
    (r"claude.3\.7", "Claude 3.7 Sonnet", "Anthropic", "2025-02-24", D, "no", "no"),
    (r"claude.3\.5", "Claude 3.5 Sonnet", "Anthropic", "2024-06-20", D, "no", "no"),
    (r"claude.3.sonnet", "Claude 3 Sonnet", "Anthropic", "2024-03-04", D, "no", "no"),
    (r"claude.3.opus|claude opus 3|^claude opus$", "Claude 3 Opus", "Anthropic", "2024-03-04", D, "no", "no"),
    (r"claude-2", "Claude 2", "Anthropic", "2023-07-11", D, "no", "no"),
    (r"gemini.3\.5.flash", "Gemini 3.5 Flash", "Google", "2026-05-19", OR, "yes", "no"),
    (r"gemini.3\.1.pro", "Gemini 3.1 Pro", "Google", "2026-02-19", OR, "yes", "no"),
    (r"gemini.3.flash", "Gemini 3 Flash", "Google", "2025-12-17", OR, "yes", "no"),
    (r"gemini 3 pro", "Gemini 3 Pro", "Google", "2025-11-18", D, "yes", "no"),
    (r"gemini 2\.5 flash lite", "Gemini 2.5 Flash-Lite", "Google", "2025-07-22", OR, "yes", "no"),
    (r"gemini.2\.5.pro", "Gemini 2.5 Pro", "Google", "2025-03-25", S, "yes", "no"),
    (r"gemini.2\.5.flash", "Gemini 2.5 Flash", "Google", "2025-04-17", D, "yes", "no"),
    (r"gemini 2\.0", "Gemini 2.0", "Google", "2025-02-05", D, "no", "no"),
    (r"gemini-1\.5-flash-8b", "Gemini 1.5 Flash-8B", "Google", "2024-10-03", D, "no", "no"),
    (r"gemini 1\.5", "Gemini 1.5 Pro", "Google", "2024-02-15", D, "no", "no"),
    (r"gemini \(bard\)", "Gemini Pro (Bard)", "Google", "2023-12-06", D, "no", "no"),
    (r"gemma.?4", "Gemma 4", "Google", "2026-04-02", OR, "no", "yes"),
    (r"gemma.?3", "Gemma 3", "Google", "2025-03-12", D, "no", "yes"),
    (r"gemma2", "Gemma 2", "Google", "2024-06-27", D, "no", "yes"),
    (r"gemma 7b", "Gemma 7B", "Google", "2024-02-21", D, "no", "yes"),
    (r"r1.distill|deepseek r1 (llama|qwen)|r1-70b|r1:32b", "DeepSeek-R1 distill", "DeepSeek", "2025-01-20", D, "yes", "yes"),
    (r"deepseek.r1|deepseek reasoner", "DeepSeek-R1", "DeepSeek", "2025-01-20", D, "yes", "yes"),
    (r"v4\.1.flash", "DeepSeek-V4.1 Flash", "DeepSeek", "2026-09-10", OR, "no", "yes"),
    (r"v3\.2-exp", "DeepSeek-V3.2-Exp", "DeepSeek", "2025-09-29", OR, "no", "yes"),
    (r"v3\.2", "DeepSeek-V3.2", "DeepSeek", "2025-12-01", OR, "no", "yes"),
    (r"v3\.1", "DeepSeek-V3.1", "DeepSeek", "2025-08-21", D, "no", "yes"),
    (r"deepseek.?v3|deepseek-chat", "DeepSeek-V3", "DeepSeek", "2024-12-26", D, "no", "yes"),
    (r"qwen3\.8-2\.4t", "Qwen3.8 2.4T", "Alibaba", "2026-08-12", OR, "no", "no"),
    (r"qwen3\.8", "Qwen3.8 Max", "Alibaba", "2026-09-03", OR, "no", "no"),
    (r"qwen3\.6", "Qwen3.6", "Alibaba", "2026-04-27", OR, "no", "yes"),
    (r"qwen3\.5-9b", "Qwen3.5 9B", "Alibaba", "2026-03-10", OR, "no", "yes"),
    (r"qwen.3\.5.397b", "Qwen3.5 397B", "Alibaba", "2026-02-16", OR, "no", "yes"),
    (r"qwen3\.5", "Qwen3.5", "Alibaba", "2026-02-25", OR, "no", "yes"),
    (r"qwen3-max", "Qwen3 Max", "Alibaba", "2025-09-05", D, "no", "no"),
    (r"qwen 3 next", "Qwen3-Next", "Alibaba", "2025-09-11", OR, "yes", "yes"),
    (r"qwen3-omni.*thinking", "Qwen3-Omni Thinking", "Alibaba", "2025-09-22", D, "yes", "yes"),
    (r"qwen3-omni", "Qwen3-Omni", "Alibaba", "2025-09-22", D, "no", "yes"),
    (r"qwen3-vl", "Qwen3-VL", "Alibaba", "2025-09-23", D, "no", "yes"),
    (r"qwen.?3", "Qwen3", "Alibaba", "2025-04-29", D, "no", "yes"),
    (r"qwq", "QwQ-32B", "Alibaba", "2025-03-06", D, "yes", "yes"),
    (r"qwen2\.5-vl", "Qwen2.5-VL", "Alibaba", "2025-01-28", D, "no", "yes"),
    (r"qwen-max", "Qwen2.5-Max", "Alibaba", "2025-01-28", D, "no", "no"),
    (r"qwen.?2\.5|therajudge|defined \(", "Qwen2.5", "Alibaba", "2024-09-19", D, "no", "yes"),
    (r"qwen-32b", "Qwen 32B (version not stated)", "Alibaba", "", "", "", "yes"),
    (r"glm-5", "GLM-5", "Zhipu", "2026-02-11", OR, "no", "yes"),
    (r"glm 4\.7", "GLM-4.7", "Zhipu", "2025-12-22", OR, "no", "yes"),
    (r"glm-zero", "GLM-Zero", "Zhipu", "2024-12-31", D, "yes", "no"),
    (r"glm-4", "GLM-4", "Zhipu", "2024-01-16", D, "no", "no"),
    (r"mistral large 3", "Mistral Large 3", "Mistral", "2025-12-01", OR, "no", "yes"),
    (r"pixtral large", "Pixtral Large", "Mistral", "2024-11-18", D, "no", "yes"),
    (r"mistral-large-2407", "Mistral Large 2", "Mistral", "2024-07-24", S, "no", "yes"),
    (r"magistral", "Magistral Small", "Mistral", "2025-07-01", S, "yes", "yes"),
    (r"mistral-small-2503", "Mistral Small 3.1", "Mistral", "2025-03-17", S, "no", "yes"),
    (r"nemo", "Mistral NeMo", "Mistral", "2024-07-18", D, "no", "yes"),
    (r"mixtral", "Mixtral 8x7B", "Mistral", "2023-12-11", D, "no", "yes"),
    (r"mistral-7b-instruct-v0\.3", "Mistral 7B v0.3", "Mistral", "2024-05-22", D, "no", "yes"),
    (r"mistral-7b-instruct-v0\.2", "Mistral 7B v0.2", "Mistral", "2023-12-11", D, "no", "yes"),
    (r"mistral.?7b", "Mistral 7B", "Mistral", "2023-09-27", D, "no", "yes"),
    (r"llama.?4|llama scout 4", "Llama 4", "Meta", "2025-04-05", D, "no", "yes"),
    (r"llama.3\.3", "Llama 3.3 70B", "Meta", "2024-12-06", D, "no", "yes"),
    (r"llama.3\.2", "Llama 3.2", "Meta", "2024-09-25", D, "no", "yes"),
    (r"llama.?3\.1", "Llama 3.1", "Meta", "2024-07-23", D, "no", "yes"),
    (r"llama.?3", "Llama 3", "Meta", "2024-04-18", D, "no", "yes"),
    (r"grok-4\.20", "Grok 4.20", "xAI", "2026-03-31", OR, "no", "no"),
    (r"grok.4\.3", "Grok 4.3", "xAI", "2026-04-30", OR, "yes", "no"),
    (r"grok-4-1-fast", "Grok 4.1 Fast", "xAI", "2025-11-19", D, "no", "no"),
    (r"grok 4", "Grok 4", "xAI", "2025-07-09", D, "yes", "no"),
    (r"grokv2", "Grok 2", "xAI", "2024-08-13", D, "no", "no"),
    (r"kimi-k2\.6", "Kimi K2.6", "Moonshot", "2026-04-20", OR, "no", "yes"),
    (r"kimi-k2", "Kimi K2", "Moonshot", "2025-07-11", OR, "no", "yes"),
    (r"doubao-seed-1-6", "Doubao Seed 1.6", "ByteDance", "2025-06-11", D, "no", "no"),
    (r"ernie-bot 4", "ERNIE Bot 4.0", "Baidu", "2023-10-17", D, "no", "no"),
    (r"step-3\.7", "Step-3.7 Flash", "StepFun", "2026-05-28", OR, "no", "yes"),
    (r"vicuna", "Vicuna-13B", "LMSYS", "2023-03-30", D, "no", "yes"),
    (r"dolly", "Dolly v2 12B", "Databricks", "2023-04-12", D, "no", "yes"),
    (r"openchat-3\.5-1210", "OpenChat 3.5", "OpenChat", "2023-12-10", S, "no", "yes"),
]
COMPILED = [(re.compile(p), rest) for p, *rest in RULES]
THINK = re.compile(r"thinking|reasoning|reasoner", re.I)


def match(name: str):
    n = re.sub(r"\s+", " ", (name or "").strip().lower())
    for rx, rest in COMPILED:
        if rx.search(n):
            return rest
    return None


def generation(release: str) -> str:
    if not release:
        return ""
    return ("to 2023-03" if release <= "2023-03-31" else "GPT-4 era (to 2024-04)" if release <= "2024-04-30"
            else "GPT-4o era (to 2024-12)" if release <= "2024-12-31" else "2025-2026")


def annotate(estimates: list[dict]) -> list[str]:
    """Adds model fields to the estimate rows; writes forms/model_releases.csv; returns names without a rule."""
    table, unmatched = {}, set()
    for e in estimates:
        r = match(e["model_name"])
        if r is None:
            unmatched.add(e["model_name"])
            r = [None, "", "", "", "", ""]
        model, dev, rel, src, reas, ow = r
        if model and THINK.search(e["model_name"]):
            reas = "yes"
        e.update({"model": model or "", "developer": dev, "release_date": rel, "release_source": src,
                  "generation": generation(rel), "reasoning_model": reas, "open_weights": ow})
        if model:
            row = table.setdefault((model, rel), {"model": model, "developer": dev, "release_date": rel,
                                                  "release_source": src, "open_weights": ow, "names_in_reports": set(),
                                                  "estimates": 0})
            row["names_in_reports"].add(e["model_name"])
            row["estimates"] += 1
    rows = sorted(table.values(), key=lambda r: (r["release_date"] or "9", r["model"]))
    with (FORMS / "model_releases.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({**r, "names_in_reports": " | ".join(sorted(r["names_in_reports"]))})
    return sorted(unmatched)
