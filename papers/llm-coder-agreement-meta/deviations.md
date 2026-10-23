# Deviations from the registered protocol (v1.0)

Every change after registration is dated, justified and listed here (protocol, item [4]), and reported in the paper.

No deviations at registration.

Administrative, not a deviation: after registration (OSF https://osf.io/z63bs, DOI 10.17605/OSF.IO/Z63BS, 2026-10-21, 13:36 UTC) the registration link was added to protocol item [2]. OSF stores `<` and `&` in three text fields as HTML entities (`&lt;`, `&amp;`: Synthesis plan, Publication bias analyses, Synthesis procedure justification); after unescaping, all 61 fields match `registration/osf.md`.

## D1. The check run's database queries used the draft term lists (found 2026-10-21, after registration)

**What the protocol says.** §10 and the registration ("Current review stage", "Search validation procedure") call `search/runs/2026-10-21-ab-check/` a check run "of the v1.0 code".

**What happened.** The database queries of that run (PubMed, Europe PMC, OpenAlex, Semantic Scholar, arXiv, DataCite; 10:26–10:50 UTC) ran before the last edit of the term lists: block 1 still lacked GPT, GPTs and the "pretrained" variants, and block 3 still had "open-ended" alone instead of the specific phrases (the edits described in §10, "Development of the strategy"). Its de-duplication, rule 6 and recall were then re-run with the final lists, and `search_log.json` was rewritten with the final lists under `_blocks`, while the per-source query strings show the draft lists. The check run is therefore a run of the draft queries with the v1.0 de-duplication, not of the v1.0 code throughout.

**Effect.** None on the review: the final search (`search/runs/2026-10-21/`, 13:40–14:10 UTC, after registration) ran the tagged v1.0 code throughout. Its recall on the seed set is 23 of 23, as in the check run. Counts: 29,171 records (check run 29,682), 12,786 unique, 753 non-study records and 5,181 records without an exact search-term match removed, **6,852 to screen** (check run 6,551). Fewer records came in, but more passed rule 6: 116 of the 6,852 records have an LLM term only through the added GPT, GPTs or "pretrained" variants; the rest of the difference comes from what the sources returned for the changed queries ("open-ended" alone mostly brought loose matches that rule 6 removed).

## D2. Number of block-3 terms in the registration text (found 2026-10-21)

The registration field "Query strings" says "Block 3: 84 psychological and clinical terms". The frozen code (`search/search.py`, `B3_PSY`) and the term list in protocol §10 have 68 terms; 84 was a miscount in `registration/osf.md`. The search ran with the 68 terms of the frozen code.

## D3. R1 screens 1,000 records directly instead of the AI passes (2026-10-22, R1's decision)

**What the protocol says.** §11b: two AI passes label every record; R1 decides every record that at least one pass keeps.

**What happened.** The AI passes ran on the Claude Max subscription and hit its session limit on 2026-10-21 at about 3,085 of 6,852 records each. On 2026-10-22, with both passes stopped (Opus 3,187 and Sonnet 3,184 records labelled), R1 chose to screen 1,000 of the remaining records himself to cut the number of AI calls. The pool was every record that neither pass had labelled and that is not in the calibration sample (3,337 records); 1,000 were drawn with `random.Random(20261024).sample` (`screening/manual_split.py` → `screening/manual/2026-10-21/manual_ids.csv`). The AI passes skip them (`llm_screen.py --exclude`); no AI label exists for these records, and none of them had one when they were drawn. R1 screens them blind in `screening/manual/2026-10-21/manual_R1_01–07.md` with the same codes; R1's decision is final, and "+" and "?" go to full text.

**Effect.** These 1,000 records get full human screening instead of the double-exclusion rule, which is at least as sensitive. They are outside the safeguard (which concerns double AI exclusions only) and outside the AI-versus-R1 agreement figures, which come from the calibration sample. The AI passes label the other 5,852 records. R1's load rises by 1,000 records; AI calls fall by 2,000.

## D4. The safeguard's blind re-screening is not carried out (2026-10-22, R1's decision)

**What the protocol says.** §11b: if a calibration record that R1 kept was excluded by both AI passes, R1 screens blind the double-excluded records that contain both an LLM term and a human-comparison term, plus a random audit of 300 of the other double exclusions.

**What happened.** The calibration (`screening/decisions/calibration_stats.json`) found 6 such records, all labelled "unsure" by R1; the AI rule kept all 31 records R1 labelled "include". For "full text" vs exclude, the rule had sensitivity 0.93 (95% CI 0.84–0.97) and specificity 0.93 (0.89–0.95) against R1. The registered targeted stratum turned out not to select: arm A of the search requires both terms, so 2,605 of the 4,178 double exclusions outside the calibration sample fall in it (2,905 records with the audit). R1 decided not to carry out the re-screening. R1 screened 1,400 records without AI labels (the calibration sample and the 1,000 records of D3) and decides every record that either pass kept and every full text.

**Effect.** The 4,178 double AI exclusions outside the calibration sample are excluded without human review. In the calibration, 6 of 302 double exclusions (2%) were R1's "unsure" and none was "include"; about 80 "unsure" records may therefore be among them. This is reported as a limitation with the calibration figures. The registered backward and forward citation searching of included studies can recover eligible studies missed at this stage.

## D5. Full-text proposals for most reports drafted by Claude Sonnet 5.5 instead of Opus 5.5 (2026-10-23)

**What the protocol says.** §3b and §11b: Claude Opus 5.5 drafts the AI proposals; `fulltext/ft_prompt.md` v1.0 names Opus 5.5 at effort high.

**What happened.** Opus drafted 209 of the 760 retrieved full texts (`fulltext/llm/ft_2026-10-21.jsonl`) and used up most of the author's Claude Max usage window within about half an hour (full texts are 20,000–70,000 tokens each). The run was stopped. The remaining reports are drafted by Claude Sonnet 5.5 at effort medium, with the same prompt and schema, after the reference list is removed from the text (`ft_screen.py --model sonnet --effort medium --strip-refs`; appendices after the references are kept). Before the switch, Sonnet drafted the same five pilot reports (`fulltext/llm/pilot_sonnet_2026-10-23.jsonl`): the same decision and reason as Opus for four; for the fifth (classroom-dialogue codes) Opus left the decision unclear and Sonnet proposed "not eligible" for the same reason (E3). Sonnet lists fewer statistics per report.

**Effect.** The proposals are drafts; R1 decides every report against the full text, and the statistics are extracted from the reports at the extraction stage, not from these drafts. The model behind each proposal is stored with it and shown in R1's decision files; R1's agreement with the proposals is reported by model.

## D6. Citation searching: two more syntheses and Semantic Scholar reference lists (2026-10-23)

**What the protocol says.** §9: backward and forward citation searching of included studies and of five syntheses (Seyler et al., 2025; Li, L., et al., 2026; Hua et al., 2025; Na et al., 2025; Flathers et al., 2026), through OpenAlex.

**What happened** (`search/citation_chase.py`; `search/runs/2026-10-23-citations/chase_log.json`). Seeds: the 411 eligible reports, the five syntheses and the two other seed-set sources (Gierbolini-Rivera et al., 2026; Kempny et al., 2026). OpenAlex had no reference list for 281 seeds (mostly arXiv and ACL papers) and no record for 13 reports; their reference lists (and, for the 13, their citing works) were taken from Semantic Scholar, which had 199 of them. For Seyler et al. (no reference list in either index), the 40 included studies resolved for the seed set were checked: none of the 9 not already found passes rule 6. New records (9,248) went through the main search's automatic rules — publication year from 2020 (3,454 removed), non-study record types (43), rule 6 (5,526) — and **225 records** (R20001–R20225) go through the same selection as the main records: both AI passes with the frozen prompt, then R1 decides every record that a pass keeps, at full text.

Both passes labelled all 225 records (`screening/llm/chase_2026-10-23_{opus,sonnet}.jsonl`, hashes committed): 70 were kept by at least one pass. Open full texts were found for 17 (`fulltext/fetch_oa.py --all-records`); Sonnet 5.5 drafted their full-text proposals (D5 settings; `fulltext/llm/ft_chase_2026-10-23.jsonl`), and R1 decides them in `fulltext/decisions/ft_R1_chase_01.md`. The other 53 are counted as sought but not retrieved without a separate title/abstract decision by R1 (it would not change the data, only the PRISMA split between "excluded at title/abstract" and "not retrieved").

**Effect.** A broader citation search than registered; its records are filtered and screened like the main search's records, except that R1 does not decide the 53 kept records without an open full text.

## D7. The estimates are drafted from the full-text proposals; one short AI pass adds moderators and risk of bias (2026-10-23)

**What the protocol says.** §11c: the AI pre-fills every field of the four tables with its source location, and R1 verifies every value. Model: Claude Opus 5.5 (§3b).

**What happened.** The full-text proposals (D5) already list 3,202 LLM–human agreement statistics for the 411 eligible reports with model, configuration, statistic, value, n, location and a verbatim quote; a second full extraction pass would read every text again for the same numbers (the five-study pilot of a full form, `extraction/draft/pilot_2026-10-23.jsonl`, needed up to 94,000 output tokens for one benchmark paper). Instead:
- `extraction/estimates_from_ft.py` turns the proposals of each study's main and attached reports into `extraction/ft_estimates.csv` (2,977 statistics in 368 studies) and checks every value against the source text by script (95.0% of values found verbatim);
- one pass of Claude Sonnet 5.5 (effort medium, reference list cut; `extraction/complete.py`, prompt `complete_prompt.md`, tag `llm-coder-agreement-extraction-prompt-v1.0`) reads each study once and drafts its tasks and moderators, a code line for each drafted estimate (inclusion, task, statistic type, model, prompting, reference, n), human–human agreement and the five risk-of-bias domains; for 17 studies whose proposals listed no statistics or hit the limit of 20, it adds the missing overall estimates with quotes;
- model attributes (developer, release date, open weights, parameters, reasoning) come from `forms/model_releases.csv`, one row per model;
- `codes.csv` (per-code κ, G8) is not drafted; G8 is tested on estimates that report both percentage agreement (or accuracy) and κ, and on the minority-class prevalence where reported.

**Effect.** The numbers come from one AI reading of each text (the full-text proposal), checked against the text by script; the moderators and risk of bias come from a second, shorter reading. The verification by R1 is described separately.

## D8. R1 reviews the coded studies instead of verifying every field; value cleaning by script (2026-10-23)

**What the protocol says.** §11c: R1 verifies every extracted value against the source and always checks the key fields.

**What happened.** R1 read the AI coding of all 372 studies in one file (`extraction/verify/audit_R1_all.md`: tasks, included and excluded values with quotes, human–human agreement, risk of bias) and listed 109 points where he disagreed. Claude checked each point against the quotes and the source tables and applied them in `extraction/r1_corrections.py` (read by `finalize.py`; R1's item numbers are kept in `forms/estimates.csv`, column `r1_item`): task types and manifest/latent codes harmonised across studies (e.g., all PsyDefConv studies T1, clinician rating scales T3, non-clinical latent ratings T1); tolerance and any-match agreement, class-specific F1, discrepancy scores and test characteristics separated from agreement statistics; cells holding several values split; values missing from the drafts added from the tables (ST027, ST090, ST134, ST216, ST240, ST266); two studies (ST314: sitcom dialogue; ST366: GPT-2 only) and four tasks excluded. Seven points were not supported by the source and were left as coded (ST010 plausibility judging is not helper-response evaluation; ST006 "HasOne" is any-match, not accuracy; ST030 ICCs are over nine models, as Table 3 states; ST154 F1 is only in a supplement not retrieved; ST208 0.893 etc. are balanced accuracy; ST218 "concordance" is not defined as Lin's CCC; ST274 both pairs are ICC(3), differing in the scoring method). Every printed value is then converted by script (`clean`): significance stars, "± SD", confidence intervals, decimal commas and percentages; bounded statistics printed on a 0–100 scale are divided by 100; ranges, bounds and cells with several values are kept but not pooled. 98.8% of the included values are found verbatim in the source texts by script.

**Effect.** R1 reviewed every study once instead of verifying every field; numbers rest on the script check against the source texts, and judgement codes on R1's review.
