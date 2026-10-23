"""Build the OSF registration package for protocol v1.0 -> registration/osf_package/ (git-ignored).

    .venv/Scripts/python.exe papers/llm-coder-agreement-meta/registration/make_osf_package.py

Output:
  Rekhert_llm_coder_agreement_protocol_v1.0.pdf   the protocol (pandoc -> docx -> LibreOffice -> PDF)
  llm-coder-agreement-prereg-v1.0.zip           protocol, forms, search and screening code, AI screener prompt, seed set,
                                                check-run and pilot logs, README and SHA-256 manifest, in the repository's folder layout
  llm_screener_prompt.md, extraction_codebook.md   loose copies for the two file fields of the OSF form
Files are taken from the commit tagged llm-coder-agreement-prereg-v1.0 (git show), so the package matches the tag byte for byte.
Template: papers/sports-betting-prevalence/registration/make_osf_package.py.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))
from llmaudit.msbuild import make_reference_docx, to_docx  # noqa: E402

OUT = HERE / "osf_package"
TAG = "llm-coder-agreement-prereg-v1.0"
P = "papers/llm-coder-agreement-meta/"
RUN = P + "search/runs/2026-10-21-ab-check/"
RUN_A = P + "search/runs/2026-10-21-check/"
FILES = [
    P + "protocol.md",
    P + "deviations.md",
    P + "forms/extraction_codebook.md",
    P + "forms/rob.md",
    P + "novelty/novelty.md",
    P + "novelty/volume_sample.csv",
    P + "search/search.py",
    P + "search/dedup.py",
    P + "search/recall.py",
    P + "search/seed_candidates.py",
    P + "search/seed_candidates.csv",
    P + "search/seed_set.csv",
    RUN + "README.md",
    RUN + "search_log.json",
    RUN + "dedup_report.json",
    RUN + "recall_seed_set.json",
    RUN_A + "search_log.json",
    RUN_A + "dedup_report.json",
    RUN_A + "recall_seed_set.json",
    P + "screening/llm_screener_prompt.md",
    P + "screening/llm_screen.py",
    P + "screening/calibration.py",
    P + "screening/screen_md.py",
    P + "screening/pilot_set.py",
    P + "screening/pilot_eval.py",
    P + "screening/pilot/pilot_set.csv",
    P + "screening/pilot/pilot_reference.csv",
    P + "screening/pilot/pilot_eval.json",
    P + "screening/llm/pilot_opus.jsonl",
    P + "screening/llm/pilot_opus.jsonl.sha256",
    P + "screening/llm/pilot_sonnet.jsonl",
    P + "screening/llm/pilot_sonnet.jsonl.sha256",
    "harness/llmaudit/__init__.py",
    "harness/llmaudit/env.py",
    "harness/llmaudit/judge.py",
]

README = """# Agreement between LLMs and human experts in coding psychological and clinical text: registration package (protocol v1.0)

Martin Rekhert, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com

Protocol v1.0 frozen before the final search and before any screening decision.
Git tag `{tag}`, commit `{commit}`.

## Contents

- `Rekhert_llm_coder_agreement_protocol_v1.0.pdf` (outside the zip) and `papers/llm-coder-agreement-meta/protocol.md`: the protocol (PRISMA-P 2015).
- `papers/llm-coder-agreement-meta/forms/`: extraction codebook (four linked tables) and risk-of-bias domains (adapted from QUADAS-2).
- `papers/llm-coder-agreement-meta/novelty/`: the novelty check (competing reviews and registrations, 2026-10-21) and the 80 manually labelled records used in the pilot of the screener prompt (`volume_sample.csv`).
- `papers/llm-coder-agreement-meta/search/`:
  - `search.py`: automated searches, arms A and B (PubMed, Europe PMC, OpenAlex, Semantic Scholar, arXiv, PsyArXiv, Crossref, DataCite, CORE);
  - `dedup.py`: de-duplication (incl. rule 2b for preprints and their published versions), removal of non-study records and of records without an exact search-term match (rule 6), and the screening list;
  - `seed_candidates.py`, `seed_candidates.csv` and `seed_set.csv`: the seed set (23 studies from the reference lists of six syntheses) and the 476 references it was drawn from; `recall.py`: recall on the seed set;
  - `runs/2026-10-21-ab-check/`: check run of the v1.0 search code (log, de-duplication report, recall 23/23); `runs/2026-10-21-check/`: the earlier arm-A-only run (recall 13/22) that led to arm B.
- `papers/llm-coder-agreement-meta/screening/`:
  - `llm_screener_prompt.md`: the AI screener's prompt and JSON schema, frozen with the protocol, with the pilot results;
  - `llm_screen.py`: its runner (two passes: Claude Opus 5.5 and Claude Sonnet 5.5);
  - `calibration.py`: draws the blind calibration sample (400 records, seed 20261022);
  - `screen_md.py`: the Markdown decision files and the safeguard (targeted blind screening plus an audit of 300);
  - `pilot_set.py`, `pilot_eval.py`, `pilot/` and `llm/pilot_*.jsonl`: pilot of the prompt on 103 records with known labels (both passes, with SHA-256 files).
- `harness/llmaudit/`: the headless Claude Code runner used by `llm_screen.py`.
- `papers/llm-coder-agreement-meta/deviations.md`: log of changes after registration (empty at registration).
- `MANIFEST.sha256`: SHA-256 of every file in this package.

## Reproducing

Python 3.12 with httpx and lxml; Claude Code CLI for the AI screener. Keys go into `.env` at the repository root: `OPENALEX_API_KEY`, `CORE_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`.

    python papers/llm-coder-agreement-meta/search/search.py --date YYYY-MM-DD
    python papers/llm-coder-agreement-meta/search/dedup.py --date YYYY-MM-DD
    python papers/llm-coder-agreement-meta/search/recall.py --date YYYY-MM-DD
    python papers/llm-coder-agreement-meta/screening/calibration.py --run YYYY-MM-DD
    python papers/llm-coder-agreement-meta/screening/llm_screen.py --run YYYY-MM-DD --pass opus
    python papers/llm-coder-agreement-meta/screening/llm_screen.py --run YYYY-MM-DD --pass sonnet

Raw search exports are not included: the databases change, so a re-run reproduces the procedure, not the exact records. The raw exports of the final search will be archived with the data release.
"""


def blob(path: str, rev: str | None) -> bytes:
    """File content as committed at rev (byte-identical to the tag), or from the working tree without a tag."""
    if rev:
        return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    return (ROOT / path).read_bytes()


def protocol_pdf(rev: str | None) -> Path:
    ref = make_reference_docx(OUT / "_reference.docx", double=False)
    md = blob(P + "protocol.md", rev).decode("utf-8")
    docx = to_docx(md, OUT / "protocol_v1.0.docx", ref, PAPER)
    soffice = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")
    subprocess.run([str(soffice), "--headless", "--convert-to", "pdf", "--outdir", str(OUT), str(docx)],
                   check=True, capture_output=True)
    pdf = OUT / "Rekhert_llm_coder_agreement_protocol_v1.0.pdf"
    (OUT / "protocol_v1.0.pdf").replace(pdf)
    for tmp in (docx, ref):
        tmp.unlink()
    return pdf


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    tagged = subprocess.run(["git", "rev-list", "-n", "1", TAG], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FILES, cwd=ROOT, capture_output=True, text=True).stdout.strip()
    rev = tagged or None
    if not tagged:
        print(f"WARNING: no tag {TAG}; packing the working tree (draft only)", file=sys.stderr)
    elif tagged != commit or dirty:
        print(f"note: HEAD {commit[:10]} differs from the tag {tagged[:10]}; packing the tagged files", file=sys.stderr)
    pdf = protocol_pdf(rev)
    readme = README.format(tag=TAG, commit=tagged or commit + " (working tree, untagged)")
    files = {f: blob(f, rev) for f in FILES}
    manifest = [f"{hashlib.sha256(b).hexdigest()}  {f}" for f, b in files.items()]
    manifest.append(f"{hashlib.sha256(readme.encode('utf-8')).hexdigest()}  README.md")
    with zipfile.ZipFile(OUT / f"{TAG}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("README.md", readme)
        for f, b in files.items():
            z.writestr(f, b)
        z.writestr("MANIFEST.sha256", "\n".join(manifest) + "\n")
    for f in (P + "screening/llm_screener_prompt.md", P + "forms/extraction_codebook.md"):
        (OUT / Path(f).name).write_bytes(files[f])
    print(f"{OUT}:")
    for p in sorted(OUT.iterdir()):
        print(f"  {p.name}  {p.stat().st_size:,} bytes")
    print(f"zip sha256: {hashlib.sha256((OUT / f'{TAG}.zip').read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
