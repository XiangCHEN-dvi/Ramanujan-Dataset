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
    num_bytes: 750289
    num_examples: 2352
  download_size: 750289
  dataset_size: 750289
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
---

# Ramanujan's Formulae

A structured, machine-readable collection of Srinivasa Ramanujan's mathematics, transcribed from Bruce C. Berndt's Ramanujan's Notebooks and Andrews & Berndt's Ramanujan's Lost Notebook.

Each record is one labeled **Entry**, **Corollary**, or **Example** from Berndt's text, in book order, with full statement text and no proofs.

## Dataset Structure

Canonical data lives in `data/` (`train.jsonl`, `schema.json`, `chapter_topics.json`). OCR drafts and local previews go in `drafts/` (gitignored). Conventions are documented in [docs/CONVENTIONS.md](docs/CONVENTIONS.md).

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Identifier such as `RN-P1-C02-Entry05-Example09` |
| `content` | string | Full mathematical statement in LaTeX (no proofs) |
| `topics` | list[string] | Chapter topic slug, e.g. `harmonic-series-and-arctan` |

### The `id` field

Each record's `id` encodes provenance and Berndt's label:

```
{WORK}-P{part}-C{chapter}-{rest}
```

| Token | Meaning |
|-------|---------|
| `RN` | Berndt, *Ramanujan's Notebooks* |
| `RLN` | Andrews & Berndt, *Ramanujan's Lost Notebook* |
| `P1` … `P5` | Part number |
| `C01` … | Chapter within that part |
| `rest` | Berndt heading: `Entry`, `Corollary`, or `Example`, with number and sub-parts |

Examples: `RN-P1-C02-Entry07-Example04` (Part I, Ch. 2, Example 4 under Entry 7); `RN-P1-C01-Entry02i` (Entry 2, part (i)). When Berndt reuses example numbers under different entries, the parent Entry is included in the ID. Full rules: [docs/CONVENTIONS.md](docs/CONVENTIONS.md).

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
# Full dataset (2352 entries) — filter in the browser UI
python scripts/preview_html.py --serve

# One chapter only (faster load)
python scripts/preview_html.py --part 1 --chapter 2 --serve

# Write drafts/preview.html and open the file directly
python scripts/preview_html.py --part 3 --chapter 19 --open
```

The page supports Part/Chapter filters, id search, pagination, and toggling raw LaTeX source per entry. Use `--serve` when opening via `file://` blocks CDN scripts.

See [docs/ISSUES.md](docs/ISSUES.md) for known ambiguities found during transcription.

## Provenance and Scope

Currently covers Berndt **Parts I–V** (Notebooks II–IV and First Notebook material, Chapters 1–39): **2352 entries** with AI-curated LaTeX.

| Part | Chapters | Records |
|------|----------|---------|
| I | 1–9 | 550 |
| II | 10–15 | 524 |
| III | 16–21 | 462 |
| IV | 22–31 | 372 |
| V | 32–39 | 444 |

PDF extraction artifacts live under `drafts/` (`_chNN_extract.txt` for Part I, `_pN_chNN_extract.txt` for Parts II–V, matching `*_records.jsonl`, and local previews). That directory is gitignored and not canonical.

Regenerate OCR drafts: `python scripts/extract_ocr_drafts.py --part 1|2|3|4|5` (requires local Berndt PDF).

## Next Steps
- Ramanujan's Lost Notebook
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
