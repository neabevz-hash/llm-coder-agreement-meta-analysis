# Check run of the v1.0 search code (2026-10-21)

Before registration: does the code run on every source, how many records reach screening, and does it find the seed set?

- `search_log.json` — query strings, record counts and times per source (arms A and B; protocol §10). CORE refuses offsets beyond about 1,100 for the LLM × agreement query (HTTP 400) and stops there; the records collected up to that point are kept.
- `dedup_report.json` — 29,682 records, 12,770 unique; removed automatically: 633 non-study records and 5,586 records without an exact search-term match (rule 6 of `dedup.py`); 6,551 to screen.
- `recall_seed_set.json` — 23 of the 23 seed studies (protocol §9).
- The screener prompt was piloted on the 23 seed records of this run and 80 manually labelled records of the novelty check: `screening/pilot/`, `screening/llm/pilot_*.jsonl` (protocol §11b).
- Raw exports, `records_unique.jsonl` and `screening.csv` are not committed (git-ignored): the final search is run again after registration.
- Arm A alone was run earlier the same day (`../2026-10-21-check/`): recall 13 of 22 eligible seeds, which led to arm B.
