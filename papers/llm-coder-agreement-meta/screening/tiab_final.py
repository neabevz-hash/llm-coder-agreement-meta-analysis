"""Final title/abstract decisions (protocol §11b; deviations D3, D4). Template: papers/sports-betting-prevalence/screening/tiab_final.py.

Every record gets its decision from one of four places:
  calibration   R1's blind label when it agrees with the AI rule (full text unless both passes exclude);
                otherwise R1's decision in the verification files (blind label and both AI labels shown);
  manual        R1's blind decision for the 1,000 records screened without AI passes (D3);
  verification  R1's decision with both AI labels shown, for records outside the sample that at least one pass kept;
  double AI exclusion  both passes excluded, outside the sample: excluded without re-screening (D4).
Records finally labelled include or unsure go to full-text screening.

Writes screening/decisions/tiab_final.csv and tiab_summary.json (numbers for PRISMA and the Methods).
Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/tiab_final.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEC = HERE / "decisions"
PASSES = ("opus", "sonnet")


def read(path: Path) -> dict[str, dict]:
    return {r["rec_id"]: r for r in csv.DictReader(path.open(encoding="utf-8-sig"))}


def full(d: str) -> bool:
    return d in ("include", "unsure")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = a.run
    screening = list(csv.DictReader((HERE.parent / "search" / "runs" / run / "screening.csv").open(encoding="utf-8-sig")))
    ai: dict[str, dict] = {}
    for p in PASSES:
        for line in (HERE / "llm" / f"{run}_{p}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                ai.setdefault(d["conv_id"], {})[p] = d["codes"]
    sample = set(json.loads((HERE / "calibration" / run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
    cal = read(HERE / "calibration" / run / "calibration_R1.csv")
    man = read(HERE / "manual" / run / "manual_R1.csv")
    ver = read(HERE / "verify" / run / "verify_R1.csv")

    rows, problems = [], []
    for s in screening:
        rid = s["rec_id"]
        lab = ai.get(rid, {})
        if rid in man:
            rule, final, where = "", man[rid]["decision"], "manual (blind, no AI pass; D3)"
        else:
            rule = "exclude" if all(lab[p]["decision"] == "exclude" for p in PASSES) else "full_text"
            if rid in sample:
                blind = cal[rid]["decision"]
                if full(blind) == (rule == "full_text"):
                    final, where = blind, "calibration (agreed with AI rule)"
                elif rid in ver:
                    final, where = ver[rid]["decision"], "calibration (resolved, labels shown)"
                else:
                    final, where = "", "MISSING"
            elif rule == "exclude":
                final, where = "exclude", "double AI exclusion (not re-screened; D4)"
            elif rid in ver:
                final, where = ver[rid]["decision"], "verification (AI labels shown)"
            else:
                final, where = "", "MISSING"
        if not final:
            problems.append(rid)
        rows.append({"rec_id": rid, "final_decision": final, "full_text": full(final), "decided_in": where, "ai_rule": rule,
                     "opus": lab.get("opus", {}).get("decision", ""), "sonnet": lab.get("sonnet", {}).get("decision", ""),
                     "opus_reason": lab.get("opus", {}).get("reason", ""), "sonnet_reason": lab.get("sonnet", {}).get("reason", ""),
                     "r1_blind": cal.get(rid, man.get(rid, {})).get("decision", ""),
                     "verify_code": ver.get(rid, {}).get("code", ""), "title": s["title"]})
    DEC.mkdir(exist_ok=True)
    with (DEC / "tiab_final.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    v_out = [r for r in rows if r["decided_in"].startswith("verification")]
    cal_res = [r for r in rows if r["decided_in"].startswith("calibration (resolved")]
    summary = {
        "run": run, "records_screened": len(rows), "missing_decisions": problems,
        "to_full_text": sum(r["full_text"] for r in rows),
        "excluded_title_abstract": sum(1 for r in rows if r["final_decision"] == "exclude"),
        "final_labels": dict(Counter(r["final_decision"] for r in rows)),
        "by_stage": {k: dict(Counter(r["final_decision"] for r in rows if r["decided_in"] == k))
                     for k in sorted({r["decided_in"] for r in rows})},
        "verification": {
            "records": len(v_out),
            "passes_agree": sum(1 for r in v_out if r["opus"] == r["sonnet"]),
            "accepted_ai_label_with_equals": sum(1 for r in v_out if r["verify_code"].startswith("=")),
            "r1_excluded_although_a_pass_kept": sum(1 for r in v_out if r["final_decision"] == "exclude"),
            "r1_excluded_although_both_kept": sum(1 for r in v_out if r["final_decision"] == "exclude"
                                                 and full(r["opus"]) and full(r["sonnet"])),
            "final_by_pass_pattern": {
                "both_kept": dict(Counter(r["final_decision"] for r in v_out if full(r["opus"]) and full(r["sonnet"]))),
                "one_kept": dict(Counter(r["final_decision"] for r in v_out if full(r["opus"]) != full(r["sonnet"]))),
            },
        },
        "calibration_resolutions": {
            "records": len(cal_res),
            "final_equals_r1_blind": sum(1 for r in cal_res if r["final_decision"] == r["r1_blind"]),
            "full_text_after_resolution": sum(r["full_text"] for r in cal_res),
        },
        "not_re_screened_double_ai_exclusions": sum(1 for r in rows if r["decided_in"].startswith("double AI exclusion")),
    }
    (DEC / "tiab_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
