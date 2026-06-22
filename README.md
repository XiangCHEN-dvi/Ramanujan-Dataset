---
language:
- en
license: mit
size_categories:
- 1K<n<10K
tags:
- mathematics
- ramanujan
- formulae
pretty_name: Ramanujan's Formulae
dataset_info:
  features:
  - name: id
    dtype: string
  - name: content
    dtype: string
  - name: topics
    sequence: string
  splits:
  - name: train
    num_bytes: 1074534
    num_examples: 3204
  download_size: 1074534
  dataset_size: 1074534
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
---

# Ramanujan's Formulae

The Indian mathematician [Srinivasa Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan) showed how much intuition can achieve in mathematics, who can be a very inspiring example for math agents.

This dataset offers a structured, machine-readable collection of Srinivasa Ramanujan's mathematics, transcribed from Bruce C. Berndt's *Ramanujan's Notebooks* and Andrews & Berndt's *Ramanujan's Lost Notebook*.

## What we collect

Every record is **one of Ramanujan's original mathematical results** — a complete statement in LaTeX, with hypotheses where needed, and **no proofs**.


| Source                               | What to include                                                                  | What to exclude                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Notebooks** (Berndt)               | Formal headings: **Entry**, **Corollary**, **Example**                           | Proofs, Berndt commentary, prose-only references without a formal heading                  |
| **Lost Notebook** (Andrews & Berndt) | Formal **Entry** labels (especially with lost-notebook page refs, e.g. `p. 207`) | Editor **Theorem**, **Lemma**, **Corollary** (proof tools, not manuscript catalog entries) |


**Lost Notebook, no Entry label:** when a chapter presents Ramanujan's manuscript as quotes or fragments (e.g. Ch. 10), we **do not** substitute editor Theorems; we **manually extract** Ramanujan's statements and assign synthetic IDs. Details and edge cases: [docs/CONVENTIONS.md](docs/CONVENTIONS.md), [docs/ISSUES.md](docs/ISSUES.md).

## Dataset Structure

Canonical data lives in `data/` (`train.jsonl`, `schema.json`, `chapter_topics.json`). OCR drafts and local previews go in `drafts/` (gitignored). Conventions are documented in [docs/CONVENTIONS.md](docs/CONVENTIONS.md).


| Field     | Type         | Description                                           |
| --------- | ------------ | ----------------------------------------------------- |
| `id`      | string       | Identifier such as `RN-P1-C02-Entry05-Example09`      |
| `content` | string       | Full mathematical statement in LaTeX (no proofs)      |
| `topics`  | list[string] | Chapter topic slug, e.g. `harmonic-series-and-arctan` |


### The `id` field

Each record's `id` encodes provenance and Berndt's label:

```
{WORK}-P{part}-C{chapter}-{rest}
```


| Token       | Meaning                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `RN`        | Berndt, *Ramanujan's Notebooks*                                                                                                                 |
| `RLN`       | Andrews & Berndt, *Ramanujan's Lost Notebook*                                                                                                   |
| `P1` … `P5` | Part number                                                                                                                                     |
| `C01` …     | Chapter within that part                                                                                                                        |
| `rest`      | Label: Notebooks — `Entry`, `Corollary`, or `Example`; Lost Notebook — `Entry` (e.g. `Entry1-2-1`) or synthetic fragment ID (e.g. `Argument01`) |


Examples: `RN-P1-C02-Entry07-Example04`; `RLN-P1-C01-Entry1-2-1`; `RLN-P1-C10-Argument01`. Full rules: [docs/CONVENTIONS.md](docs/CONVENTIONS.md).

## Usage

**From HuggingFace:**

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="data/train.jsonl", split="train")
print(dataset[0])
```

**From this repo:**

```python
from ramanujan_dataset import load_jsonl, to_hf_dataset

entries = load_jsonl()
hf_dataset = to_hf_dataset()
```

### Build and validate

```bash
python scripts/build_train.py
```

Use `python scripts/build_train.py --check-only` to validate without rebuilding.

### Manual review (rendered LaTeX)

Generate a local HTML preview with [KaTeX](https://katex.org/) rendering:

```bash
# Full dataset (3204 entries) — filter in the browser UI
python scripts/preview_html.py --serve

# One chapter only (faster load)
python scripts/preview_html.py --part 1 --chapter 2 --serve

# Write drafts/preview.html and open the file directly
python scripts/preview_html.py --part 3 --chapter 19 --open
```

The page supports Part/Chapter filters, id search, pagination, and toggling raw LaTeX source per entry. Use `--serve` when opening via `file://` blocks CDN scripts.

See [docs/ISSUES.md](docs/ISSUES.md) for known ambiguities found during transcription.

## Provenance and Scope

Currently covers Berndt **Parts I–V** (Chapters 1–39, **2352 entries**), Andrews & Berndt **Lost Notebook Parts I–V** (262 + 210 + 123 + 167 + 90 entries): **3204 entries** total.


| Work | Part | Chapters | Records |
| ---- | ---- | -------- | ------- |
| RN   | I    | 1–9      | 550     |
| RN   | II   | 10–15    | 524     |
| RN   | III  | 16–21    | 462     |
| RN   | IV   | 22–31    | 372     |
| RN   | V    | 32–39    | 444     |
| RLN  | I    | 1–18     | 262     |
| RLN  | II   | 1–16     | 210     |
| RLN  | III  | 2–10     | 123     |
| RLN  | IV   | 2–21     | 167     |
| RLN  | V    | 2–19     | 90      |


OCR drafts live under `drafts/` (gitignored). Regenerate:

- Berndt Notebooks: `python scripts/extract_ocr_drafts.py --part 1|2|3|4|5`
- Lost Notebook: `python scripts/extract_ocr_drafts_rln.py --part 1|2|3|4|5 --pdf ~/Downloads/RLN_PartI.pdf` (or `PartII` … `PartV`)

## Next Steps

- Thorough manual check

## Citation

```bibtex
@misc{ramanujan_dataset,
  author = {Xiang CHEN},
  title = {Ramanujan Formulae Dataset},
  year = {2025},
  license = {MIT},
  url = {https://github.com/xiangchen/Ramanujan-Dataset}
}
```

