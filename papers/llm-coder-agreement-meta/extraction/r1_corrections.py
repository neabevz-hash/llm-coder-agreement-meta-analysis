"""R1's review of the AI coding (chat, 2026-10-23; deviations.md, D8) and the value cleaning, applied by finalize.py.

R1 read every study (extraction/verify/audit_R1_all.md) and listed 109 points. Claude checked each against the
estimates' quotes and, where needed, the source tables; the decisions are below with R1's item numbers ("R1 33";
block 10 items as "R1 10.5"). Where the source does not support a point, the row is left as coded and the reason is
given here and in the reply to R1. clean() then turns every printed value into a number (significance stars, "± SD",
confidence intervals, decimal commas, percentages; bounded statistics printed on a 0-100 scale are divided by 100) and
marks values that are not point estimates (ranges, bounds, several values) as not pooled.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------------------------------- tasks
LAT = {"construct_type": "latent"}
T1L = {"task_type": "T1", "construct_type": "latent"}
TASKS: dict[tuple[str, str], dict] = {}      # (study, task or "*") -> changes
for sid, tasks, ch, item in [
    ("ST067", "A", T1L, "1"), ("ST069", "A", T1L, "2"), ("ST084", "*", T1L, "3"), ("ST144", "A", T1L, "4"),
    ("ST201", "A", T1L, "5"), ("ST204", "*", T1L, "6"), ("ST206", "*", T1L, "7"), ("ST269", "D", T1L, "8"),
    ("ST300", "A", {"task_type": "T2", "construct_type": "latent"}, "9"), ("ST306", "*", T1L, "10"),
    ("ST322", "*", T1L, "11"), ("ST335", "*", T1L, "12"), ("ST360", "A", T1L, "13"),
    # 14: plausibility of emotion labels is not an evaluation of helper responses (T4); kept T1, latent
    ("ST010", "H", LAT, "14"), ("ST010", "I", LAT, "14"), ("ST010", "J", LAT, "14"), ("ST010", "K", LAT, "14"),
    ("ST026", "*", T1L, "15"), ("ST117", "A", {"task_type": "T4", "construct_type": "manifest"}, "16"),
    ("ST120", "*", {"task_type": "T4", "construct_type": "manifest"}, "17"),
    ("ST252", "*", LAT, "18"), ("ST025", "A", LAT, "19"), ("ST370", "A", LAT, "19"), ("ST074", "A", LAT, "20"),
    ("ST075", "*", LAT, "20"), ("ST082", "A", {"task_type": "T3", "construct_type": "latent"}, "21"),
    ("ST091", "A", {"task_type": "T3", "construct_type": "latent"}, "22"), ("ST099", "*", LAT, "23"),
    ("ST107", "A", T1L, "24"),   # symptom presence in notes is codebook coding (T1 example in §8)
    ("ST166", "A", LAT, "25"), ("ST156", "A", LAT, "26"), ("ST213", "A", LAT, "26"), ("ST355", "A", LAT, "26"),
    ("ST018", "A", LAT, "27"), ("ST199", "*", LAT, "28"), ("ST323", "*", LAT, "28"),
    *[(s, "*", T1L, "29") for s in ("ST015", "ST106", "ST149", "ST165", "ST031", "ST177", "ST140", "ST161")],
    ("ST040", "A", {"task_type": "T3"}, "30"),   # clinician rating scales are T3 (§8 examples), as ST008, ST062
    ("ST270", "B", LAT, "31"), ("ST364", "A", T1L, "31"), ("ST291", "E", T1L, "31"), ("ST133", "*", T1L, "32"),
]:
    TASKS[(sid, tasks)] = {**ch, "r1_item": item}

TASK_EXCLUDE = {
    ("ST124", "B"): "labels are subreddit names, no human coding (R1 78)",
    ("ST233", "B"): "forecasting the next utterance's code, not coding the text (R1 81)",
    ("ST256", "B"): "reference is the writer's questionnaire score, criterion validity (E2; R1 83)",
    ("ST371", "B"): "syntactic structure, no psychological construct (E3; R1 87)",
}
STUDY_EXCLUDE = {
    "ST314": "turning points in sitcom dialogue: no psychological or clinical construct (E3; R1 86)",
    "ST366": "GPT-2 only: generative LLMs from GPT-3 on (I3); found at R1's review",
}

# ---------------------------------------------------------------------------------------------------- estimates
X = "no"
EST: dict[str, dict] = {
    "E0377": {"include": X, "exclude_reason": "76.8 is an SD in the source, not an agreement value (R1 33)"},
    **{e: {"statistic": "adjacent_agreement", "r1_item": "34"} for e in ("E1422", "E1423")},
    **{f"E{i}": {"statistic": "gwet_ac1", "value_note": "Gwet's AC2 (ordinal weights)", "r1_item": "34"}
       for i in range(1412, 1422)},
    **{f"E0{i}": {"statistic": "adjacent_agreement", "r1_item": "35"} for i in range(789, 793)},
    **{e: {"include": X, "exclude_reason": "SIRI-2 discrepancy score (lower is better), not agreement (R1 36)"}
       for e in ("E0904", "E0905", "E0906", "E0907", "E0909")},
    "E2136": {"statistic": "adjacent_agreement", "r1_item": "37"},
    "E2137": {"configuration": "Thresholded accuracy, MIRS items collapsed 1-2 vs 3-5 (binary)", "r1_item": "37"},
    **{e: {"include": X, "exclude_reason": "sensitivity, specificity, PPV: test characteristics (R1 38)"}
       for e in ("E2327", "E2328")},
    **{e: {"statistic": "any_match_agreement", "r1_item": "39"} for e in ("E2349", "E0062", "E0066")},
    **{f"E{i}": {"statistic": "mae", "value_note": "mean absolute difference", "r1_item": "40"} for i in range(2513, 2517)},
    "E1003": {"include": X, "exclude_reason": "range over variables of human-plus-LLM Fleiss kappa (R1 75)"},
    **{e: {"statistic": "f1_class", "value_note": "F1 of the 'gray' class only", "r1_item": "76"}
       for e in ("E1047", "E1048", "E1049")},
    **{f"E{i}": {"pool": X, "task_id": "A-E", "value_note": "mean over five tasks incl. TalkMoves (education)",
                 "r1_item": "79"} for i in range(1857, 1865)},
    "E0054": {"include": X, "exclude_reason": "blend with fine-tuned encoders (e5, mDeBERTa), not an LLM (R1 10.1)"},
    "E2298": {"pool": X, "value_note": "median 'concordance' over subscales; the metric is not defined in the report"},
    **{f"E{i}": {"pool": X, "task_id": "A-D", "value_note": "average accuracy over four datasets", "r1_item": "53"}
       for i in range(3232, 3236)},
    **{f"E{i}": {"icc_form": "ICC(3)", "r1_item": "85"} for i in range(2683, 2687)},
    "E0922": {"model_name": "Ensemble of Qwen2.5:14b (40% of texts) and o1-mini-2024-09-12 (60%)", "r1_item": "10.8"},
    **{e: {"model_name": "GPT-3 (text-davinci-002)", "r1_item": "10.20"} for e in ("E3270", "E3271")},
    **{f"E{i}": {"include": X, "exclude_reason": "balanced accuracy, precision and recall composites; balanced "
                 "accuracy is not extracted (D7) (R1 50)"} for i in range(2886, 2894)},
    "E2322": {"value_raw": "0.53", "value_note": "median of kappa vs each annotator (0.52-0.54)", "r1_item": "67"},
    "E2323": {"value_raw": "0.31", "value_note": "median of kappa vs each annotator (0.29-0.32)", "r1_item": "67"},
    "E3001": {"include": X, "exclude_reason": "printed values inconsistent (F1 .89 with precision .10) (R1 71)"},
}
# whole study or task rules
STUDY_STAT = {   # (study, tasks or "*", statistic in, new statistic, item)
    ("ST001", "*", "percent_agreement", "adjacent_agreement", "54"),
    *[("ST010", t, "accuracy", "any_match_agreement", "39") for t in "DEFG"],
}

# rows that hold several values: replaced by one row per value (fields override the original row)
def _s(*rows):
    return [dict(r) for r in rows]


SPLIT: dict[str, list[dict]] = {
    "E0008": _s({"value_raw": "42.9%", "configuration": "Second exam, revised gold set, wide criterion"},
                {"value_raw": "28.6%", "configuration": "Second exam, revised gold set, strict criterion"}),
    "E0375": _s({"value_raw": "78.95%", "statistic": "adjacent_agreement"}),
    "E0376": _s({"value_raw": "78.42%", "statistic": "adjacent_agreement"}),
    "E1174": _s({"value_raw": "0.88", "configuration": "therapy transcripts, depth 0"},
                {"value_raw": "0.31", "configuration": "therapy transcripts, 200 turns"}),
    "E1175": _s({"value_raw": "0.98", "configuration": "therapy transcripts, depth 0"},
                {"value_raw": "0.94", "configuration": "therapy transcripts, 200 turns"}),
    **{e: _s({"value_raw": a, "configuration": "MSJ context, depth 0"},
             {"value_raw": b, "configuration": "MSJ context, maximum depth"})
       for e, a, b in [("E1176", "0.93", "0.55"), ("E1177", "0.98", "0.63"), ("E1178", "0.96", "0.77"),
                       ("E1179", "0.96", "0.96"), ("E1180", "0.96", "0.97")]},
    **{e: _s({"task_id": "A", "value_raw": a, "n_units": "75"}, {"task_id": "B", "value_raw": b, "n_units": "60"})
       for e, a, b in [("E1438", "78.63", "67.16"), ("E1439", "78.66", "79.11"), ("E1440", "74.65", "77.78"),
                       ("E1441", "71.92", "70.44"), ("E1442", "75.89", "72.21"), ("E1443", "78.66", "79.48")]},
    "E1563": _s({"value_raw": "0.66", "reference": "single-coder", "configuration": "EXP rating vs expert rater 1"},
                {"value_raw": "0.62", "reference": "single-coder", "configuration": "EXP rating vs expert rater 2"}),
    "E1654": _s({"value_raw": "0.674", "configuration": "PsyDARA, primary code ranked first",
                 "value_note": "29/43 computed by the reviewer"},
                {"value_raw": "0.605", "model_name": "GPT-5.6 Terra (Direct)",
                 "configuration": "Direct, primary code ranked first", "value_note": "26/43 computed by the reviewer"}),
    **{e: _s({"task_id": t1, "value_raw": a, "n_units": "1000 pairs"}, {"task_id": t2, "value_raw": b, "n_units": "400 pairs"})
       for e, t1, t2, a, b in [("E1794", "A", "B", "0.487", "0.389"), ("E1795", "C", "D", "0.451", "0.523"),
                               ("E1796", "A", "B", "0.469", "0.273"), ("E1797", "C", "D", "0.531", "0.447")]},
    "E2037": _s({"value_raw": ".32", "n_units": "57", "configuration": "BGR+OSCE judge, TICKS"},
                {"value_raw": ".29", "n_units": "53", "configuration": "BGR+OSCE judge, VACC"},
                {"value_raw": ".41", "n_units": "85", "configuration": "BGR+OSCE judge, TEACH"}),
    **{e: _s({"value_raw": a, "configuration": f"{c}, EXP Mode"}, {"value_raw": b, "configuration": f"{c}, EXP Peak"})
       for e, a, b, c in [("E2140", ".70", ".66", "10-shot"), ("E2141", ".67", ".63", "7-shot, model comparison"),
                          ("E2142", ".67", ".62", "7-shot"), ("E2143", ".62", ".55", "7-shot"),
                          ("E2144", ".77", ".75", "7-shot, initial testing"), ("E2145", ".57", ".65", "7-shot, model comparison")]},
    "E2326": _s({"value_raw": "82.63%", "reference": "majority-vote", "configuration": "vs majority label"},
                {"value_raw": "77.04%", "reference": "consensus-or-adjudicated", "configuration": "vs consensus label"}),
    **{e: _s(*[{"task_id": t, "value_raw": v, "configuration": f"{lang}, {d}"}
               for t, v, d in zip("ABC", vals, ("Novelty", "Feasibility", "Goal attainment"))])
       for e, vals, lang in [("E2807", ("0.53", "0.38", "0.55"), "English-translated solutions"),
                             ("E2808", ("0.55", "0.42", "0.56"), "Traditional Chinese solutions")]},
    **{e: _s(*[{"value_raw": v, "configuration": f"observer-report vs human ratings, {tr}"}
               for v, tr in zip(vals, ("Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"))])
       for e, vals in [("E2851", ("0.55", "0.61", "0.90", "0.80", "0.25")),
                       ("E2852", ("0.44", "0.45", "0.60", "0.78", "0.59"))]},
    **{e: _s({"statistic": "rmse", "value_raw": a}, {"statistic": "mae", "value_raw": b})
       for e, a, b in [("E2912", "2.78", "2.17"), ("E2913", "2.91", "2.28")]},
    **{e: _s({"statistic": "f1_micro", "value_raw": a}, {"statistic": "f1_macro", "value_raw": b})
       for e, a, b in [("E2944", "60.2", "40.5"), ("E2945", "52.0", "38.0"), ("E2946", "63.5", "34.5"),
                       ("E2947", "52.0", "34.6"), ("E2948", "53.2", "32.6")]},
    **{e: _s({"value_raw": a, "statistic": st, "configuration": f"{cf}; first value of the cell (Table 4; the two "
              "values per cell are not labelled)"},
             {"value_raw": b, "statistic": st, "configuration": f"{cf}; second value of the cell"})
       for e, a, b, st, cf in [("E2958", "32.15", "35.98", "accuracy", "Prompted GPT-4, ACC"),
                               ("E2959", "72.07", "75.03", "adjacent_agreement", "Prompted GPT-4, ACCsoft"),
                               ("E2960", "70.53", "71.27", "accuracy", "ESC-RANK, ACC"),
                               ("E2961", "98.93", "99.17", "adjacent_agreement", "ESC-RANK, ACCsoft"),
                               ("E2962", "25.50", "21.42", "accuracy", "InternLM2 base, ACC")]},
    "E2998": _s({"value_raw": ".77"}), "E2999": _s({"value_raw": ".65"}), "E3000": _s({"value_raw": ".33"}),
    "E3002": _s({"value_raw": ".79"}),
    **{e: _s(*[{"value_raw": v, "reference": "single-coder", "configuration": f"{cf}, vs annotator {i}"}
               for i, v in enumerate(vals, 1)])
       for e, vals, cf in [("E3016", ("0.39", "0.52", "0.37"), "real data"),
                           ("E3017", ("0.70", "0.69", "0.71"), "synthetic data"),
                           ("E3018", ("0.64", "0.63", "0.40"), "synthetic data")]},
    "E3118": _s({"value_raw": "42.4", "configuration": "zero-shot, IEMOCAP 4-way, weighted accuracy"}),
    "E3119": _s({"value_raw": "52.4", "configuration": "zero-shot, EmoWOZ, macro F1"}),
    "E3120": _s({"task_id": "A", "statistic": "accuracy", "value_raw": "42.2", "configuration": "zero-shot, IEMOCAP, weighted accuracy"},
                {"task_id": "B", "statistic": "f1_macro", "value_raw": "39.0", "n_units": "NR", "configuration": "zero-shot, EmoWOZ, macro F1"}),
    "E3121": _s({"task_id": "A", "statistic": "accuracy", "value_raw": "41.8", "configuration": "zero-shot, IEMOCAP, weighted accuracy"},
                {"task_id": "B", "statistic": "f1_macro", "value_raw": "19.7", "n_units": "NR", "configuration": "zero-shot, EmoWOZ, macro F1"}),
    "E3122": _s({"task_id": "A", "statistic": "accuracy", "value_raw": "63.8", "configuration": "3-shot, IEMOCAP, weighted accuracy"},
                {"task_id": "B", "statistic": "f1_weighted", "value_raw": "66.5", "n_units": "NR", "configuration": "3-shot, EmoWOZ, weighted F1"}),
    "E3123": _s({"value_raw": "63.6", "n_units": "35", "configuration": "zero-shot, DAIC-WOZ depressed class, dev set"},
                {"value_raw": "59.3", "n_units": "47", "configuration": "zero-shot, DAIC-WOZ depressed class, test set"}),
}

# values missing from the drafts, added from the source tables (R1 10.5, 10.9, 10.11, 10.14, 82, 84)
def _add(sid, task, model, stat, val, n, conf, prompting, ref, loc, quote, item):
    return {"study_id": sid, "task_id": task, "model_name": model, "statistic": stat, "value_raw": val, "n_units": n,
            "configuration": conf, "prompting": prompting, "reference": ref, "location": loc, "quote": quote,
            "r1_item": item}


ADD = [
    _add("ST027", "B", "GPT-4o", "f1_macro", "0.426", "NR", "Task 2 depression severity, Chinese", "zero-shot", "NR",
         "Table (Task 2)", "ZH 0.433 0.438 0.428 0.426", "10.5"),
    _add("ST027", "B", "Qwen3-32B", "f1_macro", "0.390", "NR", "Task 2 depression severity, Chinese", "zero-shot", "NR",
         "Table (Task 2)", "ZH 0.417 0.413 0.409 0.390", "10.5"),
    *[_add("ST090", t, m, "accuracy", v, n, c, "zero-shot", "NR", "Table (LLM-as-judge)", q, "10.9") for t, m, v, n, c, q in [
        ("A", "O3", "0.943", "NR", "LLM-as-judge, custom dataset, hallucination", "O3 C Hal 0.943 0.107 0.076 0.089"),
        ("B", "GPT-4o-mini", "0.547", "NR", "LLM-as-judge, custom dataset, omission", "GPT-4o-mini C Omi 0.547 0.538 0.667 0.595"),
        ("B", "GPT-5", "0.533", "NR", "LLM-as-judge, custom dataset, omission", "GPT-5 C Omi 0.533 0.241 0.718 0.360"),
        ("B", "O3", "0.354", "NR", "LLM-as-judge, custom dataset, omission", "O3 C Omi 0.354 0.202 0.856 0.328"),
        ("C", "GPT-4o-mini", "0.759", "994", "LLM-as-judge, Kaggle dataset, hallucination", "GPT-4o-mini K Hal 0.759 0.800 0.016 0.032"),
        ("D", "GPT-4o-mini", "0.652", "994", "LLM-as-judge, Kaggle dataset, omission", "GPT-4o-mini K Omi 0.652 0.746 0.489 0.591")]],
    *[_add("ST134", "A", m, "f1_macro", v, n, "zero-shot", "zero-shot", "NR", "Results table", q, "10.11") for m, v, n, q in [
        ("Mistral-7B-Instruct-v0.3", "0.587", "1523 valid", "Mistral-7B-Instruct-v0.3 7B 0.511 0.587 1523"),
        ("Llama-3.2-3B-Instruct", "0.410", "1603 valid", "Llama-3.2-3B-Instruct 3B 0.412 0.410 1603"),
        ("Llama-3.2-1B-Instruct", "0.089", "1608 valid", "Llama-3.2-1B-Instruct 1B 0.060 0.089 1608")]],
    *[_add("ST216", "A", m, s, v, "1200", "zero-shot CoT, C-SSRS 0-6", "zero-shot;chain-of-thought", "NR",
           "Page 6, Table I", q, "10.14") for m, s, v, q in [
        ("Claude 3 Sonnet", "spearman", "0.8809", "SRC 0.8809 0.8843 0.8640 0.8766 0.8308"),
        ("Mistral (Pixtral Large)", "spearman", "0.8640", "SRC 0.8809 0.8843 0.8640 0.8766 0.8308"),
        ("LLaMA", "spearman", "0.8766", "SRC 0.8809 0.8843 0.8640 0.8766 0.8308"),
        ("Gemini 1.5 Pro", "spearman", "0.8308", "SRC 0.8809 0.8843 0.8640 0.8766 0.8308"),
        ("ChatGPT o3-mini", "f1_weighted", "0.7384", "F1-Score * 0.7505 0.7384 0.7208 0.6839 0.6160"),
        ("Mistral (Pixtral Large)", "f1_weighted", "0.7208", "F1-Score * 0.7505 0.7384 0.7208 0.6839 0.6160"),
        ("LLaMA", "f1_weighted", "0.6839", "F1-Score * 0.7505 0.7384 0.7208 0.6839 0.6160"),
        ("Gemini 1.5 Pro", "f1_weighted", "0.6160", "F1-Score * 0.7505 0.7384 0.7208 0.6839 0.6160")]],
    *[_add("ST266", t, m, "icc", v, "53", c, "zero-shot", "NR", "Table 3", q, "84") for t, m, v, c, q in [
        ("B", "Gemini 1.5 Pro", "0.87 (0.78 to 0.92)", "transcribed, ITI PTSD severity",
         "ITI PTSD severity ICC | 0.85 (0.76 to 0.91) | 0.87 (0.78 to 0.92) | 0.88 (0.80 to 0.93)"),
        ("B", "Gemini 1.5 Pro (direct audio)", "0.88 (0.80 to 0.93)", "direct audio, ITI PTSD severity",
         "ITI PTSD severity ICC | 0.85 (0.76 to 0.91) | 0.87 (0.78 to 0.92) | 0.88 (0.80 to 0.93)"),
        ("C", "Claude 3.5 Sonnet", "0.80 (0.67 to 0.88)", "transcribed, ITI DSO severity",
         "ITI DSO severity ICC | 0.80 (0.67 to 0.88) | 0.82 (0.72 to 0.90) | 0.86 (0.77 to 0.92)"),
        ("C", "Gemini 1.5 Pro", "0.82 (0.72 to 0.90)", "transcribed, ITI DSO severity",
         "ITI DSO severity ICC | 0.80 (0.67 to 0.88) | 0.82 (0.72 to 0.90) | 0.86 (0.77 to 0.92)")]],
]
# ST240 Table 2: kappa of the Vanilla and CoT configurations (R1 82); PsyCoT was drafted
_K240 = {"A": ("Depression", "0.337 0.374 0.535 0.331 0.335 0.610 0.256 0.282 0.544 0.343 0.370 0.616"),
         "B": ("Generalized Anxiety", "0.841 0.842 0.831 0.815 0.832 0.880 0.690 0.719 0.914 0.821 0.847 0.941"),
         "C": ("Social Anxiety", "0.736 0.719 0.792 0.644 0.665 0.777 0.467 0.482 0.893 0.644 0.644 0.914"),
         "D": ("Suicide Risk", "0.363 0.318 0.936 0.400 0.427 0.839 0.259 0.262 0.938 0.373 0.401 0.942")}
for _t, (_d, _row) in _K240.items():
    _v = _row.split()
    for _j, _m in enumerate(("GPT-4o", "Claude-3.5-sonnet", "GLM-Zero", "DeepSeek-R1")):
        for _k, (_cf, _pr) in enumerate((("Vanilla", "zero-shot"), ("CoT", "chain-of-thought"))):
            ADD.append(_add("ST240", _t, _m, "cohen_kappa", _v[3 * _j + _k], "1002", f"{_cf}, {_d}", _pr, "NR",
                            "Page 6, Table 2", f"{_d} ... κ {_row}", "82"))

FIRST_AUTHOR = {"ST238": "Elyoseph"}   # R1 88

# ---------------------------------------------------------------------------------------------------- cleaning
KAPPA = {"cohen_kappa", "fleiss_kappa", "weighted_kappa_linear", "weighted_kappa_quadratic", "weighted_kappa",
         "krippendorff_alpha", "gwet_ac1", "pabak"}
CORR = {"icc", "pearson", "spearman", "kendall", "ccc"}
DESCR = {"percent_agreement", "accuracy", "f1_macro", "f1_weighted", "f1_micro", "f1"}
BOUNDED = KAPPA | CORR | DESCR | {"precision", "recall", "adjacent_agreement", "any_match_agreement", "f1_class"}
NUM = r"[-+]?\d*\.?\d+"


def outcome(stat: str) -> str:
    return ("primary" if stat in KAPPA else "secondary" if stat in CORR else "descriptive" if stat in DESCR
            else "not pooled")


def clean(raw: str, stat: str) -> dict:
    """value, ci_low, ci_high, pool, value_note from a printed value."""
    s = (raw or "").strip()
    s = s.replace("−", "-").replace("–", "-").replace("—", "-").replace("·", ".")
    s = re.sub(r"\*+", "", s).strip()
    s = re.sub(r"(?<=\d),(?=\d)", ".", s)   # decimal comma
    note, lo, hi = [], "", ""
    if re.fullmatch(r"(?i)zero\b.*", s):
        return {"value": "0", "ci_low": "", "ci_high": "", "pool": "yes", "value_note": "printed as 'zero'"}
    if re.search(r"[<>≤≥]", s.split("(")[0]):
        return {"value": "", "ci_low": "", "ci_high": "", "pool": "no", "value_note": "bound, not a point value"}
    m = re.match(rf"^(?:[a-zA-Z]+(?:\(\d+\))?\s*=\s*)?[≈~]?\s*(?:about\s+)?({NUM})\s*(%?)(.*)$", s)
    if not m:
        return {"value": "", "ci_low": "", "ci_high": "", "pool": "no", "value_note": "not a number"}
    v, pct, rest = float(m.group(1)), m.group(2) == "%", m.group(3).strip()
    if s.startswith(("≈", "~", "about")) or "approx" in rest:
        note.append("approximate")
    ci = re.match(rf"^[\[(]\s*({NUM})\s*%?\s*(?:,|;|to|-)\s*({NUM})\s*%?\s*[\])]", rest)
    if ci:
        lo, hi = float(ci.group(1)), float(ci.group(2))
        rest = rest[ci.end():].strip()
    elif re.match(rf"^(?:-|to)\s*{NUM}", rest):
        return {"value": "", "ci_low": "", "ci_high": "", "pool": "no", "value_note": "range, not a point value"}
    if re.search(rf"(?:/|;|->|\band\b|\bvs\b)\s*\S*{NUM}", rest) and not re.match(r"^\(\s*\d+\s*/\s*\d+\s*\)", rest):
        return {"value": "", "ci_low": "", "ci_high": "", "pool": "no", "value_note": "several values in one cell"}
    if pct:
        v, lo, hi = v / 100, (lo / 100 if lo != "" else ""), (hi / 100 if hi != "" else "")
    elif stat in BOUNDED and 1 < abs(v) <= 100:
        v, lo, hi = v / 100, (lo / 100 if lo != "" else ""), (hi / 100 if hi != "" else "")
        note.append("printed on a 0-100 scale")
    elif stat in BOUNDED and abs(v) > 100:
        return {"value": "", "ci_low": "", "ci_high": "", "pool": "no", "value_note": "out of range"}
    fmt = lambda x: "" if x == "" else f"{x:.4g}"
    return {"value": fmt(v), "ci_low": fmt(lo), "ci_high": fmt(hi), "pool": "yes", "value_note": "; ".join(note)}


def apply(studies: list[dict], tasks: list[dict], estimates: list[dict]) -> tuple[list[dict], list[str]]:
    """Apply R1's review to the drafted rows; returns the new estimate rows and the keys that matched nothing."""
    unused = set(EST) | set(SPLIT) | {f"{k[0]}:{k[1]}" for k in TASKS} | {f"{k[0]}:{k[1]}" for k in TASK_EXCLUDE}
    for s in studies:
        s["excluded_r1"] = STUDY_EXCLUDE.get(s["study_id"], "")
        if s["study_id"] in FIRST_AUTHOR:
            s["first_author"] = FIRST_AUTHOR[s["study_id"]]
    for t in tasks:
        for key in ((t["study_id"], t["task_id"]), (t["study_id"], "*")):
            if key in TASKS:
                t.update(TASKS[key])
                unused.discard(f"{key[0]}:{key[1]}")
        t["excluded_r1"] = TASK_EXCLUDE.get((t["study_id"], t["task_id"]), "")
        if t["excluded_r1"]:
            unused.discard(f"{t['study_id']}:{t['task_id']}")
    out = []
    for e in estimates:
        e.setdefault("r1_item", "")
        e.setdefault("pool", "")
        e.setdefault("value_note", "")
        for sid, tk, st, new, item in STUDY_STAT:
            if e["study_id"] == sid and (tk == "*" or e["task_id"] == tk) and e["statistic"] == st:
                e["statistic"], e["r1_item"] = new, item
        if e["study_id"] == "ST021" and e["statistic"] == "percent_agreement" and "within-1" in e.get("quote", ""):
            e["statistic"], e["r1_item"] = "adjacent_agreement", "33"
        if e["estimate_id"] in EST:
            e.update(EST[e["estimate_id"]])
            unused.discard(e["estimate_id"])
        if e["estimate_id"] in SPLIT:
            unused.discard(e["estimate_id"])
            for j, part in enumerate(SPLIT[e["estimate_id"]], 1):
                out.append({**e, **part, "estimate_id": f"{e['estimate_id']}.{j}", "r1_item": e["r1_item"] or "split"})
            continue
        out.append(e)
    for i, a in enumerate(ADD, 1):
        out.append({"estimate_id": f"A{i:03d}", "include": "yes", "exclude_reason": "NA", "source": "r1_review",
                    "n_examples": "NR", "authors_primary": "no", "prevalence": "NR", "mean_llm": "NA",
                    "mean_human": "NA", "pool": "", "value_note": "", **a})
    excl_s = {s["study_id"]: s["excluded_r1"] for s in studies if s["excluded_r1"]}
    excl_t = {(t["study_id"], t["task_id"]): t["excluded_r1"] for t in tasks if t["excluded_r1"]}
    ttype = {(t["study_id"], t["task_id"]): t["task_type"] for t in tasks}
    for e in out:
        if e["study_id"] in excl_s:
            e["include"], e["exclude_reason"] = "no", excl_s[e["study_id"]]
        elif (e["study_id"], e["task_id"]) in excl_t:
            e["include"], e["exclude_reason"] = "no", excl_t[(e["study_id"], e["task_id"])]
        e["task_type"] = ttype.get((e["study_id"], e["task_id"]), e.get("task_type", ""))
        c = clean(e["value_raw"], e["statistic"])
        pool_override = e.get("pool") == "no"
        e["value"], e["ci_low"], e["ci_high"] = c["value"], c["ci_low"], c["ci_high"]
        e["value_note"] = "; ".join(x for x in (e.get("value_note", ""), c["value_note"]) if x)
        e["pool"] = "no" if (pool_override or c["pool"] == "no" or e["include"] != "yes") else "yes"
        e["outcome"] = outcome(e["statistic"])
    return out, sorted(unused)
