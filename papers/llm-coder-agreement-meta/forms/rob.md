# Risk of bias: five domains (v1.0, frozen with protocol v1.0; protocol §14, adapted from QUADAS-2)

Each domain is rated low / high / unclear. The AI drafts each rating with a supporting quote; R1 decides. No summary score; domains enter as moderators and sensitivity filters.

| Domain | Low | High | Unclear |
| --- | --- | --- | --- |
| 1. Unit selection | evaluation units are random, consecutive or all units of a defined set | units hand-picked, selected for clarity or difficulty, or selection unexplained while a larger pool existed | selection not described |
| 2. LLM configuration | prompt and settings fixed before the evaluation units, or tuned only on a separate development set; and all tested configurations reported (or only one tested) | tuned on the evaluation units, or only the best of several configurations reported | not stated how the configuration was chosen |
| 3. Human reference | coders trained or expert, coding independently of each other and without seeing LLM output, with human–human reliability reported on these units | a single untrained coder, coders who saw LLM output before coding, or no reliability reported for the reference | partly reported |
| 4. Data contamination | evaluation texts and labels private, or first released after the model's training cutoff | evaluation texts and labels public before the model's training cutoff (public benchmark or published dataset) | release date or cutoff unknown |
| 5. Reporting | exact model version, run date, settings and prompt (or a link to it) reported | model version or prompt not reported | partly reported |

Notes:
- Domain 4 uses the model's documented training cutoff; when several models are evaluated, the rating is per estimate (`estimates.csv`) and the study rating is the worst one.
- Domains 1–3 feed GRADE risk of bias (protocol §17); domain 2 also tests G9; domain 4 is a moderator and a sensitivity filter.
