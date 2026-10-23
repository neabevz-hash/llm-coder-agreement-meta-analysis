"""Link the eligible reports into studies and extraction jobs (protocol §8 E7, §11a "Linked versions", codebook `report_ids`).

A study is one evaluation: LLMs and human coders on one set of text units. Reports are linked into one study when
(a) they are versions of the same evaluation: preprint and published article, conference and extended journal version,
    thesis and article, conference abstract and article, a plain-language summary; or
(b) the same team evaluates LLMs on the same units against the same human coding in companion reports.
Different teams on the same public dataset (GoEmotions, AnnoMI, ESConv, PsyDefConv...) stay separate studies; the dataset
is recorded in studies.csv (`dataset`). Links were set from the AI full-text proposals (field possible_duplicate), title
and author matches, and checked against the text: authors, units, n and reported values.

Every report of a study is listed in study_map.csv; only the reports that can add estimates are sent to the extractor
("attached"); versions whose values are all in the main report are "listed" (linked, not sent), to save input tokens.
A report holding two separate evaluations on different units (a thesis) gives two studies (EXTRA_STUDIES). A study with
two task types is split into two study_ids at extraction (codebook, `task_type`).
Pairs that only might overlap (same team, units possibly shared) stay separate and are listed in POSSIBLE for R1.

Writes extraction/study_map.csv (one row per study x report) and extraction/jobs.json (one job per study).
Template: papers/ai-dependence-correlates/extraction/make_study_map.py.
Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/extraction/make_study_map.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records, rec_num  # noqa: E402

# main report, attached (sent to the extractor), listed (linked, values all in the main or attached reports), reason
GROUPS = [
    ("R7526", [], ["R9004"], "Bellaiche et al.: two copies of the Scientific Reports article (same title, authors and "
     "7,854 emotion-regulation ideas)"),
    ("R7331", [], ["R12278"], "DepreSym (Pérez et al.): arXiv preprint 2023 (R12278) and Language Resources and Evaluation "
     "article 2025 (R7331), same 21,580 sentences"),
    ("R9635", [], ["R11812", "R5157"], "Relins et al., 500 Boston Police narratives: CrimRxiv/arXiv preprint (R11812), "
     "Journal of Quantitative Criminology article (R9635) and the authors' plain-language summary (R5157)"),
    ("R2480", [], ["R11249"], "Na et al., multi-session treatment outcome: 2024 conference version (R11249, 30 sessions) "
     "and the extended LRE 2026 version (R2480, 110 sessions)"),
    ("R3684", [], ["R10542"], "Lyu et al., AIHQ scoring: arXiv preprint (R10542) and Psychological Assessment article (R3684)"),
    ("R0317", [], ["R10863"], "Valentine et al., clinician bias in psychiatric notes: LREC-COLING 2024 paper (R10863) and "
     "the extended LRE 2026 article (R0317), same 39 sentences"),
    ("R7322", [], ["R9283"], "Moreno-Ortiz, Severance emotions: Research Square preprint (R9283) and Corpus Pragmatics "
     "article (R7322)"),
    ("R1082", [], ["R8880"], "Lamboy et al., resilience in life-story interviews: Research Square preprint (R8880) and "
     "journal article (R1082)"),
    ("R10135", [], ["R10136"], "Thotapalli et al., youth emergency triage: medRxiv preprint (R10136) and PCN Reports "
     "article (R10135)"),
    ("R2683", [], ["R0772"], "Kim et al., multi-view attention MIL for cognitive distortions: ACL 2026 proceedings (R2683) "
     "and the Underline record of the same paper (R0772)"),
    ("R9978", ["R9055"], ["R9979", "R10661"], "MIBot/AutoMISC (University of Toronto), the same 821 utterances of 10 MIBot "
     "transcripts: Ali et al. (R9978, NLPAI4Health 2025; R9979, Ali's thesis) compare models with consensus labels; "
     "Mahmood et al. (R9055, arXiv/ACL Findings 2025; R10661, Mahmood's thesis, identical values) compare AutoMISC "
     "(GPT-4o) with each of four annotators"),
    ("R9476", [], ["R10978"], "Patra et al., social support and isolation in psychiatric notes: arXiv preprint (R10978) "
     "and JAMIA article (R9476)"),
    ("R10973", [], ["R12582"], "Singh et al., emotion triggers: arXiv/NAACL 2024 paper (R12582) and the author's thesis, "
     "its extended version (R10973)"),
    ("R1726", [], ["R7937"], "Donnelly et al., safety plan scoring: medRxiv preprint (R7937) and JMIR Mental Health "
     "article (R1726)"),
    ("R3342", [], ["R8824"], "Kormilitzin et al., self-harm in EHRs: medRxiv preprint (R8824) and JMIR Mental Health "
     "article (R3342), same 1,352 notes"),
    ("R4533", [], ["R9748"], "Osian et al., Prevention of Future Deaths reports: arXiv preprint (R9748) and BMJ Mental "
     "Health article (R4533)"),
    ("R6421", [], ["R6427"], "Yang et al., SLE Reddit posts: medRxiv preprint (R6427) and Lupus Science & Medicine "
     "article (R6421)"),
    ("R12045", [], ["R12046"], "Wiest et al., suicidality in admission notes: medRxiv preprint (R12046) and British "
     "Journal of Psychiatry article (R12045), same 100 notes"),
    ("R5732", [], ["R8326"], "Takahashi et al., medical interview transcripts: preprint (R8326) and JMIR Medical "
     "Education article (R5732), same 7 transcripts"),
    ("R10006", [], ["R10007"], "Steinbrenner et al., negative psychotherapy experiences: Research Square preprint (R10007) "
     "and npj Mental Health Research article (R10006)"),
    ("R9558", [], ["R12528"], "Prinzing et al., spirituality from text: PsyArXiv preprint (R12528) and Journal of "
     "Personality article (R9558)"),
    ("R7490", ["R11107"], [], "Balt et al., the same 38 psychological autopsy interviews: conference abstract with "
     "zero-shot Llama 3 (R11107) and the Frontiers in Public Health article with few-shot coding (R7490)"),
    ("R4589", [], ["R11445"], "Park et al., harmful suicide content (452 Korean posts): arXiv preprint (R11445) and JMIR "
     "Medical Informatics article (R4589)"),
    ("R0470", [], ["R0469"], "Chen et al., therapist-client dynamics: the arXiv paper (R0470) is Chapter 2 of Chen's "
     "thesis (R0469), same validation values"),
    ("R10127", [], ["R10130"], "Thomas et al., NGASR suicide risk in krisenchat transcripts: Research Square preprint "
     "(R10130) and Scientific Reports article (R10127)"),
    ("R4523", [], ["R0222"], "Al-Shamaileh et al., Arabic emotion classification of 1,002 sentences: Research Square "
     "preprint (R0222) and the extended Scientific Reports article (R4523)"),
    ("R4970", ["R1986"], [], "Francese, Iannotta et al., TALD scoring of interviews with 33 patients with schizophrenia: "
     "conference abstract (R1986) and Multimedia Tools and Applications article (R4970)"),
    ("R2117", ["R2175"], ["R8764"], "LlaMADRS (Kebe, Girard et al.), CAMI interviews: earlier 2025 version (R8764, 236 "
     "interviews), TACL 2026 version (R2117, 541 sessions, 25 models) and the companion paper for clinical researchers "
     "on the same data and method (R2175)"),
    ("R9403", ["R11584"], [], "Niu et al., GPT-4 emotion annotation on 500-sample subsets of ISEAR, SemEval and "
     "GoEmotions: Interspeech 2024 paper (R11584) and the extended IEEE Transactions on Affective Computing article (R9403)"),
    ("R9566", [], ["R12379"], "Qi, Fu et al., SOS-HL-1K and SocialCD-3K: Research Square/arXiv preprint (R12379) and "
     "Bioengineering article (R9566)"),
    ("R1327", ["R1329"], [], "Soria, UC Berkeley Social Networks Study (UCNets), the same two-coder human consensus: R1327 "
     "compares 8 LLMs on 3,208 responses, the companion study R1329 18 LLMs on 525 of them"),
    ("R3196", ["R7028"], [], "Lodrant, STIPO-R-A interviews with adolescents: the pilot conference paper (R7028, GPT-4o, "
     "25 participants) used a subset of the thesis data (R3196)"),
    ("R10981", [], ["R12271"], "Brown et al., MI reflections: the GPT-4 evaluation of 610 reflections in the arXiv paper "
     "(R10981) and in Brown's thesis (R12271), identical values"),
    ("R0807", ["R4135"], [], "Badawi, Rahimi, Dolatabadi et al. (York University, Vector Institute), the same expert "
     "ratings of mental-health responses: R4135 reuses R0807's closed-source judge results and adds trained judges"),
    ("R0810", ["R2481"], [], "PsyDefConv/PsyDefDetect organisers (Na et al.): the dataset paper (R0810) and the shared-task "
     "overview (R2481) on the same test set"),
    ("R8687", [], ["R9079"], "Mao et al., confidence-aware fine-grained debate: the arXiv paper (R8687) is Chapter 6 of "
     "Mao's thesis (R9079)"),
]

# A second, separate evaluation inside a report that already belongs to a study: (report, scope)
EXTRA_STUDIES = [
    ("R0469", "Chapter 4 only (therapist interactions with LLM-simulated couple agents; LLM stage labels against human "
              "coding). Chapter 2 is the study of R0470; Chapter 3 compares an LLM evaluator with another LLM."),
]

# What to extract when it is not simply "every eligible evaluation in the main report"
SCOPE = {
    "R9978": "Two evaluations on the same 821 utterances: (a) R9978, models against consensus labels; (b) the attached "
             "R9055, AutoMISC (GPT-4o) against each of four annotators, with their human-human agreement. Extract both; "
             "each value once.",
    "R7490": "Two configurations on the same 38 interviews: few-shot coding in R7490 and zero-shot Llama 3 in the "
             "attached abstract R11107. Extract both.",
    "R4970": "Take the values from R4970; from the attached abstract R1986 only values not in R4970.",
    "R2117": "Take the estimates from R2117 (541 sessions). From the attached R2175 only values that are not in R2117 "
             "(other statistics, models or subsets); note in the draft where the two disagree.",
    "R9403": "R9403 extends R11584 on the same subsets. Take each value once; where both report the same configuration "
             "and statistic, use R9403 and note a difference.",
    "R1327": "Extract both reports: R1327 (3,208 responses) and the attached R1329 (525 responses, more models).",
    "R3196": "Extract both: the thesis R3196 and the pilot R7028 (GPT-4o on 25 participants of the same data).",
    "R0807": "Closed-source judges (Claude-3.7-Sonnet, GPT-4o, o4-mini, Gemini) from R0807 only; from the attached R4135 "
             "take only its own judges (TheraJudge and the Qwen2.5-7B variants).",
    "R0810": "From R0810 take the LLM baselines. From the attached overview R2481 take the organisers' baselines that are "
             "not in R0810 and the results of participating teams that have no system paper of their own in this review; "
             "the system papers R0481, R3584, R4485, R4743, R5350, R5444 and R5748 are separate studies.",
    "R0470": "Chapter 2 of Chen's thesis (R0469) is this paper; extract from R0470.",
}

# Facts the extractor cannot see in the text
JOB_NOTES: dict[str, str] = {
    "R6639": "R1 included this dissertation. The AI full-text note says Study 1 (Chapter 1, mathematics problem-posing "
             "codes) is not psychological and Study 2 (Chapter 2, students' affect toward mathematics) is the eligible "
             "evaluation.",
    "R3861": "R1 is the author of this study (protocol §3c): own_study = yes.",
}

# Possible overlaps kept as separate studies; shown to R1
POSSIBLE = [
    (["R7986", "R7988"], "Elyoseph et al., news articles on suicide coded against the WHO guidelines: R7988 (120 articles, "
     "40 of them Hebrew) builds on the 40-article Hebrew study R7986; whether the Hebrew articles are the same is not stated"),
    (["R4121", "R9403"], "Niu et al., GPT-4 zero-shot emotion labels: R4121 uses the full test splits of GoEmotions, "
     "SemEval-2018 and ISEAR, R9403 (with R11584) 500-sample subsets of them"),
    (["R2682", "R2683"], "J.S. Kim et al., cognitive-distortion detection: different methods and LLM baselines, partly "
     "the same test data (KoACD, Therapist QA)"),
    (["R5453", "R7861"], "Dauphin, Siefert et al., SCORS-G ratings of narratives: R7861 uses 58 narratives from the "
     "SCORS-G manual and training materials, R5453 1,966 narratives from three samples, one rated by the scale's developers"),
    (["R8347", "R9566"], "Qi et al., SocialCD-3K posts: R8347 re-annotated them with standardised labels (another human "
     "reference)"),
    (["R3526", "R6639"], "University of Delaware mathematics-metaphor project: R6639 (Ma's dissertation, 814 descriptions) "
     "and R3526 (Zhang, Hwang, Ma, Cai; 2,265 responses) may share student responses"),
]

# First authors where the record's author field is wrong (Underline and repository records), from the full texts
FIRST_AUTHOR = {
    "R0011": "Zhao", "R0716": "Kim", "R0725": "Zhong", "R0741": "Randhawa", "R0761": "Xu", "R0772": "Kim",
    "R0791": "Wuraola", "R0798": "Demeocq", "R0807": "Badawi", "R0810": "Na", "R7028": "Lodrant", "R7398": "She",
    "R7423": "Mitran", "R7438": "Haydarov",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    eligible = set(eligible_reports())

    seen = {}
    for main_rec, att, lst, _ in GROUPS:
        for k in [main_rec, *att, *lst]:
            if k not in eligible:
                raise SystemExit(f"{k} is not an eligible report")
            if k in seen:
                raise SystemExit(f"{k} is in two groups ({seen[k]}, {main_rec})")
            seen[k] = main_rec
    for members, _ in POSSIBLE:
        for k in members:
            if k not in eligible:
                raise SystemExit(f"{k} (POSSIBLE) is not an eligible report")

    group_of = {m: (att, lst, why) for m, att, lst, why in GROUPS}
    singles = sorted(eligible - set(seen), key=rec_num)
    studies = [(m, "") for m in [*group_of, *singles]] + [(k, scope) for k, scope in EXTRA_STUDIES]
    studies.sort(key=lambda s: (rec_num(s[0]), s[1]))
    study_id = {(m, scope): f"ST{i:03d}" for i, (m, scope) in enumerate(studies, 1)}
    main_study = {m: sid for (m, scope), sid in study_id.items() if not scope}

    possible_of: dict[str, list[str]] = {}
    for members, why in POSSIBLE:
        for k in members:
            sk = seen.get(k, k)
            others = ", ".join(f"{m} ({main_study[seen.get(m, m)]})" for m in members if m != k)
            possible_of.setdefault(sk, []).append(f"possible overlap with {others}: {why}")

    jobs, rows = [], []
    for m, scope in studies:
        sid = study_id[(m, scope)]
        att, lst, why = group_of.get(m, ([], [], "")) if not scope else ([], [], "")
        jobs.append({"job_id": sid, "study_id": sid, "main": m, "attached": att, "listed_only": lst, "link_reason": why,
                     "scope": scope or SCOPE.get(m, "Extract every eligible evaluation in the main report."),
                     "job_notes": JOB_NOTES.get(m, ""), "possible_overlap": possible_of.get(m, []) if not scope else []})
        for k, role in [(m, "main"), *[(x, "attached") for x in att], *[(x, "listed") for x in lst]]:
            u = recs[k]
            rows.append({"study_id": sid, "rec_id": k, "role": role,
                         "first_author": FIRST_AUTHOR.get(k) or (u.get("first_author") or ""), "year": u.get("year") or "",
                         "doi": u.get("doi") or "", "title": u.get("title") or "",
                         "link_reason": why if (att or lst) else "", "scope": scope,
                         "possible_overlap": " | ".join(possible_of.get(m, [])) if not scope else ""})
    with (HERE / "study_map.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (HERE / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    linked = sum(1 for j in jobs if j["attached"] or j["listed_only"])
    print(f"{len(eligible)} reports -> {len(jobs)} studies ({linked} with linked reports, "
          f"{sum(len(j['attached']) for j in jobs)} attached and {sum(len(j['listed_only']) for j in jobs)} listed reports; "
          f"{len(EXTRA_STUDIES)} extra study inside a thesis); {len(POSSIBLE)} possible overlaps for R1")


if __name__ == "__main__":
    main()
