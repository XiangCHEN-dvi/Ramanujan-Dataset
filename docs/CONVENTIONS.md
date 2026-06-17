# Dataset Conventions

This document records the agreed workflow for transcribing Ramanujan's mathematics from Berndt's edited volumes into `data/train.jsonl`.

## Scope

Primary source: Bruce C. Berndt, *Ramanujan's Notebooks* (Parts I–V). Future work will add George E. Andrews & Bruce C. Berndt, *Ramanujan's Lost Notebook*.

Each JSONL record is one labeled item from Berndt's text: an **Entry**, **Corollary**, or **Example**.

## Record schema

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Stable identifier (see below) |
| `content` | yes | Full mathematical statement in LaTeX, including hypotheses; no proofs |
| `topics` | yes | Chapter topic slug(s); one slug per chapter |

Proofs, Berndt commentary, bibliographic notes, and solution steps are excluded from `content`.

## Ordering

Records appear in **Berndt book order** within each chapter: the order items first appear in the edited volume, not notebook page order.

## What counts as one record

Include every Berndt heading of the form `Entry …`, `Corollary …`, or `Example …`.

| Case | Rule |
|------|------|
| `Entry 2(i)`, `Entry 2(ii)` | One record each |
| `Example 1(i)`, `Example 1(ii)` | One record each |
| Unnumbered corollary after Entry *n* | `…-Entry{n}-Corollary` |
| Numbered corollary under Entry *n* | `…-Entry{n}-Corollary{k}` |
| Unnumbered example after Entry *n* | `…-Entry{n}-Example` |
| Numbered example under Entry *n* | `…-Entry{n}-Example{k}` |
| Example before any entry in the chapter | `…-Example{seq}` with sequential `seq` in chapter |
| Entry with sub-parts `9(i)`, `9(ii)` | `…-Entry09i`, `…-Entry09ii` |

`Entry`, `Corollary`, and `Example` are written **directly adjacent** to their numbers and roman-numeral sub-parts (no hyphen). Hyphens separate major segments only.

Exclude:

- Proofs (`Proof. …`)
- Section introductions without an Entry/Corollary/Example label
- Prose-only references such as "In Corollary 1, Ramanujan states …" when Berndt does not give a formal heading

## ID format

```
{WORK}-P{part}-C{chapter:02d}-{rest}
```

| Token | Meaning |
|-------|---------|
| `RN` | *Ramanujan's Notebooks* (Berndt) |
| `RLN` | *Ramanujan's Lost Notebook* (Andrews & Berndt) |
| `P1` … `P5` | Berndt part number |
| `C01` … | Chapter number within that part |

Examples:

```
RN-P1-C01-Example01
RN-P1-C01-Entry02i
RN-P1-C01-Entry02-Corollary01
RN-P1-C02-Entry01-Corollary
RN-P1-C02-Entry05-Example09
RN-P1-C02-Entry09-Corollary03
RLN-P1-C03-Entry12
```

**Duplicate example numbers** (common in Chapter 2) are disambiguated by the parent Entry in the ID, not by chapter-wide sequence alone.

There is no `source` field; provenance is encoded in `id`.

## Topics

One slug per chapter, taken from the chapter title:

| Part | Ch | Slug |
|------|----|------|
| I | 1 | `magic-squares` |
| I | 2 | `harmonic-series-and-arctan` |
| II | 10 | `hypergeometric-series-i` |
| II | 11 | `hypergeometric-series-ii` |
| II | 12 | `continued-fractions` |
| II | 13 | `integrals-and-asymptotic-expansions` |
| II | 14 | `infinite-series` |
| II | 15 | `asymptotic-expansions-and-modular-forms` |
| III | 16 | `q-series-and-theta-functions` |
| III | 17 | `fundamental-properties-of-elliptic-functions` |
| III | 18 | `jacobian-elliptic-functions` |
| III | 19 | `modular-equations-degrees-3-5-7` |
| III | 20 | `modular-equations-higher-composite-degrees` |
| III | 21 | `eisenstein-series` |
| IV | 22 | `elementary-results` |
| IV | 23 | `number-theory` |
| IV | 24 | `ramanujan-theory-of-prime-numbers` |
| IV | 25 | `theta-functions-and-modular-equations` |
| IV | 26 | `inversion-formulas-lemniscate-and-allied-functions` |
| IV | 27 | `q-series` |
| IV | 28 | `integrals` |
| IV | 29 | `special-functions` |
| IV | 30 | `partial-fraction-expansions` |
| IV | 31 | `elementary-and-miscellaneous-analysis` |
| V | 32 | `continued-fractions-supplement` |
| V | 33 | `elliptic-functions-alternative-bases` |
| V | 34 | `class-invariants` |
| V | 35 | `values-of-theta-functions` |
| V | 36 | `modular-equations-supplement` |
| V | 37 | `infinite-series-supplement` |
| V | 38 | `approximations-and-asymptotic-expansions` |
| V | 39 | `miscellaneous-results-first-notebook` |

Full mapping: `data/chapter_topics.json`.

## Content guidelines

- Use LaTeX for mathematics.
- Include verbal hypotheses ("For each positive integer n", "Let x and a be real", etc.).
- For construction examples (magic squares), state the problem and give the resulting array in a `array` or `matrix` environment.
- For methods (e.g. Entry 12), state the method and the equation it applies to, not Berndt's numerical commentary.
- If OCR omits a formula, reconstruct from Berndt's numbered equation (e.g. (3.1)) and mark for review if uncertain.

## Workflow

1. Extract chapter text from PDF: `python scripts/extract_pdf.py --chapter N --output drafts/chN.txt` (or use `scripts/extract_ocr_drafts.py` to write under `drafts/` automatically).
2. List all Entry / Corollary / Example headings in order.
3. Transcribe each statement into `scripts/entries/pN_chNN.py` (e.g. `p1_ch03.py`, `p2_ch10.py`).
4. Regenerate JSONL: `python scripts/build_train.py`
5. Validate only: `python scripts/build_train.py --check-only`
6. Note ambiguities in `docs/ISSUES.md`.

## Directory layout

| Path | Tracked | Contents |
|------|---------|----------|
| `data/` | yes | `train.jsonl`, `schema.json`, `chapter_topics.json` |
| `drafts/` | no (gitignored) | OCR extract text, draft JSONL, table page images, HTML preview |
| `scripts/entries/` | yes | Curated LaTeX source modules |

## Known limitations

See `docs/ISSUES.md` for problems discovered while applying these rules to Parts I–V (Ch.1–39).

PDF extraction outputs under `drafts/` (`_chNN_extract.txt`, `_pN_chNN_extract.txt`, matching `*_records.jsonl`, previews) are temporary OCR drafts for curation reference; canonical data always comes from `scripts/entries/pN_chNN.py`.
