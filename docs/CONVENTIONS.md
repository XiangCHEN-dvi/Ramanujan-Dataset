# Dataset Conventions

This document records the agreed workflow and **collection criteria** for transcribing Ramanujan's mathematics from Berndt's edited volumes into `data/train.jsonl`.

## Collection criteria

**Core principle:** each record is one of **Ramanujan's original mathematical results**. Proofs, editor commentary, and mathematics added by the editors for exposition are excluded.

### Ramanujan's Notebooks (Berndt, Parts I–V)

Berndt's `Entry` / `Corollary` / `Example` labels form a catalog of Ramanujan's notebook material (~3900 results). The labels are Berndt's, but the content is Ramanujan's.

| Include | Exclude |
|---------|---------|
| Every formal heading `Entry …`, `Corollary …`, or `Example …` | `Proof. …` and proof steps |
| Edge cases documented in `ISSUES.md` (e.g. prose-cited results given a formal ID when clearly Ramanujan's) | Prose-only references without a formal heading ("In Corollary 1, Ramanujan states …") |
| | Editor reformulations Berndt declines to state separately (e.g. "Corollary 2 is simply an alternative formulation of Entry 1") |
| | Section introductions, bibliographic notes, numerical tables unless part of the stated result |

### Ramanujan's Lost Notebook (Andrews & Berndt)

The Lost Notebook edition is structured as a proof monograph. Only **`Entry X.Y.Z`** headings reliably point to formulas on the lost-notebook manuscript (often with page references such as `p. 207`).

| Include | Exclude |
|---------|---------|
| Formal **`Entry X.Y.Z`** with manuscript provenance | **`Theorem`**, **`Lemma`**, **`Corollary`** — these are overwhelmingly editorial (proof infrastructure, cited literature, or results explicitly noted as not in the manuscript) |
| **Manually mined** statements from manuscript fragments when a chapter has no `Entry` labels (synthetic IDs; see below) | Cross-chapter reference lists (e.g. Ch. 18 citing `Entry 12.2.1` from another chapter) |

**Chapters without `Entry` labels** (e.g. Ch. 10, empirical Rogers–Ramanujan fragments on pp. 358–361): do **not** include editor Theorems used to interpret the fragments. Instead, extract Ramanujan's own assertions, calculations, and quoted formulas from the manuscript text; assign synthetic IDs such as `RLN-P1-C10-Argument01` or `RLN-P1-C10-Formula0203`; document provenance in `ISSUES.md`.

Granularity: one record per **standalone mathematical proposition** (identity, evaluation, construction problem, asymptotic claim), not one record per entire narrative section.

## Scope

Primary sources:

- Bruce C. Berndt, *Ramanujan's Notebooks* (Parts I–V)
- George E. Andrews & Bruce C. Berndt, *Ramanujan's Lost Notebook* (Parts I–V)

Each JSONL record is one Ramanujan result as selected above.

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

### Notebooks (RN)

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

### Lost Notebook (RLN)

Include:

- Every formal **`Entry X.Y.Z`** whose chapter number matches the chapter being transcribed (first component of the label equals the chapter number)
- Manually mined records from manuscript fragments when no `Entry` heading exists (synthetic `rest` segment; see Collection criteria)

Exclude:

- `Theorem`, `Lemma`, and `Corollary` headings (editorial; see Collection criteria)
- Proofs and editor commentary
- Cross-chapter citations presented only as references to entries in other chapters

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
RN-P1-C02-Entry05-Example09
RLN-P1-C01-Entry1-2-1
RLN-P1-C16-Entry16-1-3
RLN-P1-C10-Argument01
```

**Notebooks IDs** use Berndt's integer Entry numbers and roman-numeral sub-parts.

**Lost Notebook IDs** for formal entries use Berndt's `chapter.section.number` label: `Entry1-2-1` is Entry 1.2.1 in Part I, Chapter 1.

**Synthetic RLN IDs** (mined fragments) use a descriptive token after the chapter prefix, e.g. `Argument01`, `Formula0203` (book equation number). Document each in `ISSUES.md`.

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
| RLN I | 1 | `rogers-ramanujan-continued-fraction` |
| RLN I | 2 | `explicit-evaluations-rogers-ramanujan-continued-fraction` |
| RLN I | 3–18 | see `data/chapter_topics.json` (`RLN-P1-C03` … `RLN-P1-C18`) |
| RLN II | 1–16 | see `data/chapter_topics.json` (`RLN-P2-C01` … `RLN-P2-C16`) |
| RLN III | 2–10 | see `data/chapter_topics.json` (`RLN-P3-C02` … `RLN-P3-C10`) |
| RLN IV | 2–21 | see `data/chapter_topics.json` (`RLN-P4-C02` … `RLN-P4-C21`) |
| RLN V | 2–19 | see `data/chapter_topics.json` (`RLN-P5-C02` … `RLN-P5-C19`); Ch. 1 intro excluded |

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
| `scripts/entries/` | yes | Curated LaTeX source modules (`pN_chNN.py` for RN, `rln_pN_chNN.py` for RLN) |

### Lost Notebook workflow

1. OCR (Entry-only): `python scripts/extract_ocr_drafts_rln.py --part 1|2|3|4 --pdf ~/Downloads/RLN_PartI.pdf` (or `PartII` … `PartIV`)
2. Bootstrap (optional): `python scripts/jsonl_to_module_rln.py --part 1|2 --chapter N`
3. Filter to Entry-only: `python scripts/filter_rln_entry_only.py --chapter N`
4. Curate LaTeX in `scripts/entries/rln_pN_chNN.py`; mine fragments where no Entry labels exist (e.g. RLN P1 Ch. 10; RLN P3 Ch. 5/10; RLN P4 Ch. 11/15–17/21; RLN P5 Ch. 14)
5. Rebuild: `python scripts/build_train.py`

## Known limitations

See `docs/ISSUES.md` for problems discovered while applying these rules to Parts I–V (Ch.1–39).

PDF extraction outputs under `drafts/` (`_chNN_extract.txt`, `_pN_chNN_extract.txt`, matching `*_records.jsonl`, previews) are temporary OCR drafts for curation reference; canonical data always comes from `scripts/entries/pN_chNN.py`.
