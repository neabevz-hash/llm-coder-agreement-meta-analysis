"""Calibration results (protocol, section 11b): R1's blind labels against the two AI passes.

Checks both AI label files against the SHA-256 committed before unblinding, then reports for each pass (opus, sonnet)
and for the AI rule (full text unless both passes exclude):
- Cohen's kappa for include / unsure / exclude (each pass);
- kappa, Gwet's AC1 and PABAK for "full text" (include or unsure) vs exclude, with bootstrap 95% CIs for kappa and AC1;
- sensitivity and specificity against R1 for "full text", with Clopper-Pearson 95% CIs;
- the safeguard: calibration records that R1 labelled include or unsure and both passes labelled exclude.
Template: papers/sports-betting-prevalence/screening/calibration_stats.py (PABAK added, as protocol §11b lists it).

Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/calibration_stats.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "harness"))
from llmaudit.agreement import bootstrap_ci, cohen_kappa, gwet_ac1, pabak, percent_agreement  # noqa: E402

PASSES = ("opus", "sonnet")


def binom_cdf(k: int, n: int, p: float) -> float:
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def clopper_pearson(x: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact binomial CI by bisection (no scipy in the environment)."""
    if n == 0:
        return float("nan"), float("nan")

    def solve(f, lo=0.0, hi=1.0):
        for _ in range(80):
            mid = (lo + hi) / 2
            if f(mid):
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2

    lower = 0.0 if x == 0 else solve(lambda p: 1 - binom_cdf(x - 1, n, p) >= alpha / 2)
    upper = 1.0 if x == n else solve(lambda p: binom_cdf(x, n, p) <= alpha / 2)
    return lower, upper


def full(d: str) -> str:
    return "full_text" if d in ("include", "unsure") else "exclude"


def binary_stats(a2: list[str], b2: list[str]) -> dict:
    tp = sum(x == "full_text" and y == "full_text" for x, y in zip(a2, b2))
    fn = sum(x == "full_text" and y == "exclude" for x, y in zip(a2, b2))
    tn = sum(x == "exclude" and y == "exclude" for x, y in zip(a2, b2))
    fp = sum(x == "exclude" and y == "full_text" for x, y in zip(a2, b2))
    return {"agreement": percent_agreement(a2, b2), "kappa": cohen_kappa(a2, b2), "kappa_ci": bootstrap_ci(cohen_kappa, a2, b2),
            "ac1": gwet_ac1(a2, b2, ["full_text", "exclude"]),
            "ac1_ci": bootstrap_ci(gwet_ac1, a2, b2, categories=["full_text", "exclude"]),
            "pabak": pabak(a2, b2, ["full_text", "exclude"]),
            "sensitivity": tp / (tp + fn) if tp + fn else float("nan"), "sensitivity_ci": clopper_pearson(tp, tp + fn),
            "specificity": tn / (tn + fp) if tn + fp else float("nan"), "specificity_ci": clopper_pearson(tn, tn + fp),
            "counts": {"tp": tp, "fn": fn, "tn": tn, "fp": fp}}


def load_pass(run: str, p: str) -> tuple[dict[str, str], str]:
    path = HERE / "llm" / f"{run}_{p}.jsonl"
    sha_path = path.with_name(path.name + ".sha256")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    committed = json.loads(sha_path.read_text(encoding="utf-8"))["sha256"] if sha_path.exists() else None
    if committed != digest:
        sys.exit(f"{path.name} does not match the committed hash ({committed} vs {digest})")
    first: dict[str, dict] = {}   # earliest label per record if a pass ever labelled one twice
    for line in path.open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            if d["conv_id"] not in first or d["judged_at"] < first[d["conv_id"]]["judged_at"]:
                first[d["conv_id"]] = d
    return {k: v["codes"]["decision"] for k, v in first.items()}, digest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--decisions", help="CSV from screen_md.py parse (default screening/calibration/<run>/calibration_R1.csv)")
    a = ap.parse_args()
    ai, digests = {}, {}
    for p in PASSES:
        ai[p], digests[p] = load_pass(a.run, p)
    sample = json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"]
    dec_path = Path(a.decisions) if a.decisions else HERE / "calibration" / a.run / "calibration_R1.csv"
    r1 = {r["rec_id"]: r["decision"] for r in csv.DictReader(dec_path.open(encoding="utf-8-sig"))}
    missing = [i for i in sample if not r1.get(i)]
    if missing:
        sys.exit(f"R1 has no decision for {len(missing)} calibration records: {missing[:10]}")
    ids = [i for i in sample if all(i in ai[p] for p in PASSES)]
    unlabeled = [i for i in sample if i not in ids]
    cats3 = ["include", "unsure", "exclude"]
    a3 = [r1[i] for i in ids]
    a2 = [full(x) for x in a3]
    out = {"run": a.run, "ai_labels_sha256": digests, "n_calibration": len(sample), "n_compared": len(ids),
           "calibration_records_without_ai_label": unlabeled, "passes": {}}
    for p in PASSES:
        b3 = [ai[p][i] for i in ids]
        out["passes"][p] = {
            "three_labels": {"agreement": percent_agreement(a3, b3), "kappa": cohen_kappa(a3, b3),
                             "kappa_ci": bootstrap_ci(cohen_kappa, a3, b3),
                             "confusion": {f"R1_{x}": {f"AI_{y}": sum(u == x and v == y for u, v in zip(a3, b3)) for y in cats3} for x in cats3}},
            "full_text_vs_exclude": binary_stats(a2, [full(x) for x in b3])}
    rule = ["exclude" if all(ai[p][i] == "exclude" for p in PASSES) else "full_text" for i in ids]
    out["ai_rule_full_text_unless_both_exclude"] = binary_stats(a2, rule)
    out["passes_agreement_full_text_vs_exclude"] = {
        "agreement": percent_agreement([full(ai["opus"][i]) for i in ids], [full(ai["sonnet"][i]) for i in ids]),
        "kappa": cohen_kappa([full(ai["opus"][i]) for i in ids], [full(ai["sonnet"][i]) for i in ids])}
    false_negatives = [i for i, r in zip(ids, rule) if full(r1[i]) == "full_text" and r == "exclude"]
    out["safeguard_triggered"] = bool(false_negatives)
    out["rule_false_negatives"] = false_negatives
    out["single_pass_false_negatives"] = {p: [i for i in ids if full(r1[i]) == "full_text" and ai[p][i] == "exclude"] for p in PASSES}
    dest = HERE / "decisions" / "calibration_stats.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    n_ft = sum(x == "full_text" for x in a2)
    print(f"{len(ids)} calibration records compared; R1 full text {n_ft}, R1 exclude {len(ids) - n_ft}")
    for p in PASSES:
        f2 = out["passes"][p]["full_text_vs_exclude"]
        print(f"{p}: kappa3 {out['passes'][p]['three_labels']['kappa']:.2f}; full text vs exclude kappa {f2['kappa']:.2f}, "
              f"AC1 {f2['ac1']:.2f}, PABAK {f2['pabak']:.2f}, sensitivity {f2['sensitivity']:.2f} {tuple(round(v, 2) for v in f2['sensitivity_ci'])}, "
              f"specificity {f2['specificity']:.2f} {tuple(round(v, 2) for v in f2['specificity_ci'])}")
    r = out["ai_rule_full_text_unless_both_exclude"]
    print(f"AI rule: sensitivity {r['sensitivity']:.2f} {tuple(round(v, 2) for v in r['sensitivity_ci'])}, "
          f"specificity {r['specificity']:.2f} {tuple(round(v, 2) for v in r['specificity_ci'])}, kappa {r['kappa']:.2f}, AC1 {r['ac1']:.2f}")
    print("safeguard TRIGGERED: R1 screens all double-excluded records blind" if false_negatives
          else "safeguard not triggered", false_negatives or "")
    print(f"-> {dest}")


if __name__ == "__main__":
    main()
