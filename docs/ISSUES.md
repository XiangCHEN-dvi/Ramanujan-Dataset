# Issues found

Issues discovered when building the dataset. Parts I–V (Ch.1–39) all have AI-curated LaTeX in `scripts/entries/pN_chNN.py`.

# Part I

Issues discovered when building Part I of the dataset. All nine chapters now have AI-curated LaTeX (Ch.1–2 manual + curated; Ch.3–9 curated from OCR drafts).

## Summary counts

| Chapter | Records | Source | Berndt intro count (approx.) |
|---------|---------|--------|------------------------------|
| 1 | 19 | Manual LaTeX | 43 |
| 2 | 59 | Manual LaTeX | 68 |
| 3 | 58 | AI curated LaTeX | 68 |
| 4 | 37 | AI curated LaTeX | 42 |
| 5 | 53 | AI curated LaTeX | 94 |
| 6 | 43 | AI curated LaTeX | 86 |
| 7 | 83 | AI curated LaTeX | 86 |
| 8 | 84 | AI curated LaTeX | 86 |
| 9 | 114 | AI curated LaTeX | 86 |
| **Total** | **550** | | **759** |

Our counts differ from Berndt's intro totals because (a) we include only formal `Entry` / `Corollary` / `Example` headings, (b) prose-only references are excluded, and (c) curated chapters split monolithic OCR records into sub-parts (e.g. Ch.9 Entry 6(i)–(viii)).

---

## Chapters 1–2 (manual transcription)

### ISSUE-01: Prose-only corollaries in Chapter 1

Chapter 1 opens with two corollaries about arithmetic progressions in magic squares. Berndt describes them as "In Corollary 1, Ramanujan states …" without a formal `Corollary 1.` heading. **Excluded** under the current rule (formal headings only).

### ISSUE-02: Section templates without labels

Section 4 gives a general 3×3 template; Section 8 gives 5×5 templates. These are not labeled Entry/Corollary/Example. **Excluded**; the labeled examples in those sections are included.

### ISSUE-03: Missing Entry 6(i) in OCR

Berndt labels Entry 6(i) for the middle-four-elements identity, but PDF text extraction often merges it into Section 6 prose. Included manually from Berndt's statement.

### ISSUE-04: OCR drops formulae

Several formulae appear only as equation numbers in the PDF text layer, e.g. Entry 3 `(3.1)`, Entry 11 Corollaries 2–3, Example 5–8 in Section 5 of Chapter 2. Content was reconstructed from Berndt's numbered equations and standard references.

### ISSUE-05: Duplicate "Example 1" labels

Chapter 2 reuses Example 1 many times under different entries. IDs use parent Entry (`RN-P1-C02-Entry07-Example01`, etc.) to disambiguate.

### ISSUE-06: Entry 10 and Entry 12 are methods, not single formulae

Entry 10 states four partial-fraction expansions in one entry. Entry 12 describes Bernoulli's root-finding method. Both are kept as **one record each** with full statement text, per the Entry label rule.

### ISSUE-07: Example 8 missing in Chapter 2, Section 5

Berndt lists Examples 1–7, 9, 10 under Entry 5; Example 8 appears in the notebook but is easy to miss in the PDF. Included as `RN-P1-C02-Entry05-Example08` from the identity in Berndt's proof discussion.

### ISSUE-08: Entry 9 Corollaries 1–2

Sinh and cosh product representations are described as "Corollaries 1 and 2 of Entry 9" in prose before Corollary 3 receives a formal heading. Included as separate records with standard product formulae.

### ISSUE-09: Magic square example sub-parts

Examples such as "Construct magic squares with (i) r = 15 and (ii) r = 27" are stored as **one record** with both parts in `content`, because Berndt uses a single Example heading.

### ISSUE-10: Numerical examples under Entry 12

Examples 1–4 (polynomial roots) and 1–2 (e^x = 2, e^{-x} = x) include Ramanujan's convergent lists. Content states the equation and that Ramanujan gives convergents; full float tables are omitted as non-essential.

---

## Chapters 3–9 (curated from OCR)

### ISSUE-11: Content quality

All Part I chapters now have AI-curated LaTeX in `scripts/entries/p1_chNN.py`. Proofs and Berndt commentary are excluded; false Ramanujan claims are noted where Berndt flags them.

### ISSUE-11a: Chapter 3 curated (2025-06)

Chapter 3 was re-processed with the same curated workflow as Ch.1–2: formulae reconstructed from Berndt equation numbers where OCR failed, proofs excluded, proper `$...$` / `\sum` / `\Gamma` notation. Two records added that OCR skipped: `RN-P1-C03-Entry09-Examplei` and `RN-P1-C03-Entry09-Exampleiii`. Entry 10 statement trimmed to the theorem (Berndt proof sketch removed from `content`).

### ISSUE-11b: Chapter 4 curated (2025-06)

37 records with proper LaTeX. Added `RN-P1-C04-Entry10-Example02` (OCR skipped). Entry 8 Corollary 2 notes Berndt's remark that Ramanujan's claim is false for $n>2$. Entries 1 and 9 remain excluded (no formal headings in Berndt).

### ISSUE-11c: Chapter 5 curated (2025-06)

53 records; removed all `-dup` IDs from OCR. Added `RN-P1-C05-Entry01i` and `Entry01ii` (Bernoulli-number expansion cited before Entry 2). Added `RN-P1-C05-Entry19iii`. Entry 29 marked as false in `content`. Entries 9–10 (Bernoulli definitions), 21, 23, 24 still excluded (prose-only or no formal heading).

### ISSUE-11d: Chapter 6 curated (2025-06)

43 records; removed all `-dup` IDs. Entry 11 kept as the Euler transform only (proof sketch excluded). Examples 1–2 at chapter open retained as `RN-P1-C06-Example01/02`. Entries 2–3, 4(i)/4(iii), 5, 8, 9, 12, 13 still excluded per ISSUE-16 (prose-only or trivial).

### ISSUE-11e: Chapter 7 curated (2025-06)

83 records (+17 from OCR). Split `Entry11-Corollary` into five sub-records; added `Entry11-Example01`–`07`, `Entry12-Example01`–`03`, `Entry14-Corollary01`, `Entry22-Example`, `Entry25-Corollary01`. Renamed mis-parented `Entry20-Corollary` → `Entry21-Corollary`. Entry 9, Entry 21 (main), Entry 24 excluded (prose-only). Entry 4 Corollaries 6–8 note Ramanujan's incompatible asymptotics.

### ISSUE-11f: Chapter 8 curated (2025-06)

84 records (+4 net). Removed all `-dup` IDs; fixed `Entry13-Example13i` → `Entry13-Examplei` (etc.). Split Entry 14 into `Entry14i`–`viii` ($A_1,\ldots,A_{10}$). Reconstructed stubs (Entry 3, 15, 18). Entry 5 notes Ramanujan's sign error. Entry 17(v) notes divergent series. Entry 1 excluded.

### ISSUE-11g: Chapter 9 curated (2025-06)

114 records (+54 from OCR). Split monolithic entries (1–2, 5–7, 9–11, 24–26, 30–31, 33); added Entry 4(i)/(ii), Entry 13, Entry 28a, Entry 32 corollaries/examples, Entry 35 Examples (i)–(iv). Removed `-dup` IDs and Quarterly Reports crossover prose. Entry 3 marked false; Entry 27 Example (i) misprint noted.

### ISSUE-12: Auto-extractor limitations (OCR drafts only)

The scripts `scripts/extract_entries.py` and `scripts/extract_ocr_drafts.py` write **non-canonical** drafts to `drafts/_chNN_extract.txt` (Part I) or `drafts/_pN_chNN_extract.txt` (Parts II–V) and matching `*_records.jsonl`. They do **not** update `scripts/entries/` or `data/train.jsonl`.

Known extractor limitations:

- Stops each record at `Proof.` / `First proof` / `Second proof`.
- Skips Berndt prose cross-references (e.g. "Entry 10 is enormously interesting …").
- Drops records with fewer than 10 characters of statement text after extraction.
- Does not reconstruct formulae from numbered equations `(n.m)` when OCR omits the formula body.
- Applies only basic OCR→LaTeX substitutions (`\log`, `\Gamma`, `\sum`, etc.).

Regenerate OCR drafts: `python scripts/extract_ocr_drafts.py` (Part I, Ch.3–9) or `python scripts/extract_ocr_drafts.py --part 2` (Part II, Ch.10–15). Requires local Berndt PDF.

### ISSUE-13: Duplicate IDs (`-dup` suffix) — resolved

OCR drafts used `-dup1` / `-dup2` where the same heading appeared twice. All curated chapters (3–9) now have no `-dup` IDs.

### ISSUE-14: Short content records

After curation, **10 records** have fewer than 40 characters; all are complete one-line statements (mostly numeric Examples or corollaries such as `$\log 2=\varphi(2)$`). The OCR-era stub problem (~42 records with lost formulae) was resolved during Ch.3–9 curation.

### ISSUE-15: Missing entries — no formal heading in PDF

| Chapter | Missing Entry # | Reason |
|---------|-----------------|--------|
| 4 | 1, 9 | No `Entry 1.` / `Entry 9.` heading (curated; still excluded) |
| 5 | 9, 10, 21, 23, 24 | Entry 9–10 are Bernoulli definitions cited in prose; others lack formal headings (Entry 1 added as 01i/01ii) |
| 6 | 1–3, 5, 8, 9, 12, 13 | Prose-only per ISSUE-16; Entry 4(i) and 4(iii) still missing |
| 7 | 9, 21 (main), 24 | Prose-only; Entry 21 Corollary retained |
| 8 | 1 | Chapter opens at Entry 2 |
| 9 | — | Entry 4(i)/(ii) added in curated version |

### ISSUE-16: Prose-only entries excluded (Chapter 6)

Chapter 6 has several items Berndt discusses without formal headings:

- **Entry 2** — Euler–Maclaurin summation (prose: "simply another form of …").
- **Entry 3** — Definition of `\varphi(-x)` (prose: "used only to make a definition").
- **Entry 8** — Particular Euler–Maclaurin instance (prose).
- **Entry 4(i)**, **Entry 4(iii)**, **Entry 10(i)**, **Entry 10(iii)** — Partially prose-only or trivial; extractor got 4(ii) and 10(ii) only.

### ISSUE-17: Chapter-level Examples without parent Entry

Chapter 6 opens with `Example 1` and `Example 2` (series constants) before any Entry heading. Stored as `RN-P1-C06-Example01`, `RN-P1-C06-Example02` per convention.

### ISSUE-18: Prose-only Examples excluded (Chapter 3)

Under Entry 15, Berndt references Example 3(i)–3(viii) and 4(ii)–4(iv) in prose; only those with formal headings are included (3(iii), 3(v), 3(vii), 4(i)). Entry 9 Examples (i) and (iii) were missing in OCR but **added** in curated Ch.3 (`RN-P1-C03-Entry09-Examplei`, `Entry09-Exampleiii`).

### ISSUE-19: OCR typos in headings

PDF text layer garbles some labels, affecting ID assignment:

- `Entry 14(i}.` → normalized to `Entry14i` (Chapter 6).
- `Entry lO(ii)` → `Entry10ii` via `lO`→`10` normalization.
- `Example (bI)` vs `(b1)` — letter/ digit confusion.

### ISSUE-20: Wrong parent Entry for nested items

When Examples appear after Entry sub-parts (e.g. 9(vii)), parent is correctly reset to base `Entry09`. Chapter 8 `Entry13-Example13i` IDs were corrected to `Entry13-Examplei` in curated version.

### ISSUE-21: Long entries truncated (OCR era — resolved)

Very long statements were truncated when the auto-extractor hit the next heading or proof marker. Curated `scripts/entries/p1_chNN.py` files contain full statements for Ch.3–9.

### ISSUE-22: Chapter 9 density and Quarterly Reports overlap

Chapter 9 is the longest (126 PDF pages). Quarterly Reports crossover material at the end of Berndt Ch.9 is excluded from curated records (e.g. former `Entry35-Examplea/b` from QR prose).

### ISSUE-23: Corollaries with empty statement lines — resolved

Some OCR corollaries had headings only (e.g. `RN-P1-C07-Entry04-Corollary01`). Curated versions reconstruct the statement from Berndt's text.

### ISSUE-24: Chapter 5 Entry numbering

Chapter 5 begins with Entry 2(i)–2(ii) in notebook order; Entry 1 was added as `RN-P1-C05-Entry01i` and `Entry01ii` from Berndt's prose Bernoulli expansion. Entry 9–10 (Bernoulli definitions) remain excluded (prose only).

### ISSUE-25: Chapter 4 missing Entry 9 and Example 2 under Entry 10

Entry 9 has no formal heading (still excluded). Entry 10 Example 2 added as `RN-P1-C04-Entry10-Example02` in curated version.

---

## Workflow notes

- **Do not edit** `data/train.jsonl` directly; edit `scripts/entries/pN_chNN.py`, then run `python scripts/build_train.py`.
- OCR drafts in `drafts/` are gitignored and superseded by curated entry modules.
- `python scripts/build_train.py` rebuilds JSONL and validates schema, duplicate IDs, and topic slugs.

---

# Part II

Issues discovered when building Part II (Berndt Chapters 10–15). All six chapters have AI-curated LaTeX in `scripts/entries/p2_chNN.py`.

## Summary counts (Part II)

| Chapter | Title | Records | OCR draft | Berndt intro (approx.) |
|---------|-------|---------|-----------|------------------------|
| 10 | Hypergeometric Series, I | 113 | 103 | 116 |
| 11 | Hypergeometric Series, II | 92 | 47 | 103 |
| 12 | Continued Fractions | 96 | 82 | 113 |
| 13 | Integrals and Asymptotic Expansions | 85 | 42 | 92 |
| 14 | Infinite Series | 82 | 62 | 87 |
| 15 | Asymptotic Expansions and Modular Forms | 56 | 29 | 94 |
| **Total** | | **524** | **365** | **605** |

Combined dataset: **1074** records (550 Part I + 524 Part II).

### ISSUE-P2-01: Chapter 10 curated (2025-06)

113 records (+10 from OCR). Added `Entry06b`, `Entry18ii`, `Entry07-Example14`–`Example19`, `Entry13-Example01/02`. Entry 34 unnumbered corollary excluded (prose only).

### ISSUE-P2-02: Chapter 11 severe OCR under-capture

92 records (+45 from OCR). Entries 2–7 and most of 17–36 were missing. Fixed bogus `Entry32-Exampleii` merge.

### ISSUE-P2-03: Chapter 12 continued fractions

96 records (+14 from OCR). Removed all `-dup` IDs; added Entry 15 parts, Entry 44(ii), Entry 45(i–ii).

### ISSUE-P2-04: Chapter 13 integrals and asymptotics

85 records (+43 from OCR). Added Entry 4 Example, Entry 24(i) corollary, Entry 25 Examples; split sub-parts throughout.

### ISSUE-P2-05: Chapter 14 infinite series

82 records (+20 from OCR). Replaced Entry 20 `-dup` corollaries; added Entry 19(iii), Entry 21(i); fixed Entry 25(x)–25(xii).

### ISSUE-P2-06: Chapter 15 modular forms

56 records (+27 from OCR). Split Entry 12(i)–(x) from Entry 13; excluded prose-only Entries 2, 5, 6, 9.

Bootstrap OCR modules: `python scripts/jsonl_to_module.py --part 2 --chapter N`.

---

# Part III

Issues discovered when building Part III (Berndt Chapters 16–21, Notebook IV). All six chapters have AI-curated LaTeX in `scripts/entries/p3_chNN.py`.

## Summary counts (Part III)

| Chapter | Title | Records | OCR draft |
|---------|-------|---------|-----------|
| 16 | q-Series and Theta-Functions | 77 | 58 |
| 17 | Fundamental Properties of Elliptic Functions | 153 | 38 |
| 18 | The Jacobian Elliptic Functions | 53 | 34 |
| 19 | Modular Equations (Degrees 3, 5, 7) | 116 | 23 |
| 20 | Modular Equations (Higher/Composite) | 27 | 29 |
| 21 | Eisenstein Series | 36 | 9 |
| **Total** | | **462** | **191** |

Combined dataset: **1536** records (550 Part I + 524 Part II + 462 Part III).

### ISSUE-P3-01: Chapter 16 q-series

77 records (+19 from OCR). Full theta-function \(f(a,b)\), Rogers–Ramanujan, Entry 22 split into \(\varphi,\psi,f,\chi\). Removed proof fragments and `-dup` IDs.

### ISSUE-P3-02: Chapter 17 elliptic functions

153 records (+115 from OCR). Severe under-capture; background curation added Entries 5, 11–12, full Entry 7 sub-parts, Entry 8 theta products, etc.

### ISSUE-P3-03: Chapter 18 Jacobian functions

53 records (+19 from OCR). Entry 14 introduces \(\mathrm{sn},\mathrm{cn},\mathrm{dn}\); Entry 16 corrected to \(\pi-\theta\).

### ISSUE-P3-04: Chapter 19 modular equations (3, 5, 7)

116 records (+93 from OCR). Largest expansion; degree-3/5/7 modular equations with all sub-parts. Entry 19(ii),(v),(vii) reciprocals corrected per Berndt proofs.

### ISSUE-P3-05: Chapter 20 higher modular equations

27 records (net −2 from OCR after removing bogus `Entry00-Corollary00` and `-dup` IDs). Berndt uses combined Entry headings (e.g. Entries 1–7); fewer discrete records than page count suggests.

### ISSUE-P3-06: Chapter 21 Eisenstein series

36 records (+27 from OCR). All Entries 1–11 with roman-numeral sub-parts; Final Entry as Entry 12(i–ii).

Bootstrap: `python scripts/jsonl_to_module.py --part 3 --chapter N`. OCR: `python scripts/extract_ocr_drafts.py --part 3`.

---

# Part IV

Issues discovered when building Part IV (Berndt Chapters 22–31, unorganized Notebook II/III material). All ten chapters have AI-curated LaTeX in `scripts/entries/p4_chNN.py`.

## Summary counts (Part IV)

| Chapter | Title | Records | OCR draft |
|---------|-------|---------|-----------|
| 22 | Elementary Results | 37 | 33 |
| 23 | Number Theory | 85 | 39 |
| 24 | Ramanujan's Theory of Prime Numbers | 17 | 14 |
| 25 | Theta-Functions and Modular Equations | 86 | 57 |
| 26 | Inversion Formulas (Lemniscate) | 10 | 8 |
| 27 | q-Series | 9 | 8 |
| 28 | Integrals | 46 | 28 |
| 29 | Special Functions | 37 | 14 |
| 30 | Partial Fraction Expansions | 15 | 5 |
| 31 | Elementary and Miscellaneous Analysis | 30 | 49 |
| **Total** | | **372** | **255** |

Combined dataset: **1908** records.

### ISSUE-P4-01: Part IV PDF chapter detection

Part IV uses running headers (`22. Elementary Results`) instead of `CHAPTER 22` page starts. `extract_pdf.chapter_page_ranges_part4()` detects these; standard `CHAPTER` detection finds only Ch.29 and 31.

### ISSUE-P4-02: Entry page-reference headings

Part IV headings use `Entry N (p. XXX).` format. `extract_entries.py` was extended with optional `(p. …)` / `(pp. …)` page refs in ENTRY/COROLLARY/EXAMPLE regexes.

### ISSUE-P4-03: Chapter 23 number theory

85 records (+46 from OCR). Added Entry 30, Entry 43 sub-parts, Example blocks under Entries 18/42/44.

### ISSUE-P4-04: Chapter 25 theta/modular

86 records (+29 from OCR). Full P–Q eta modular equations block (Entries 51–72).

### ISSUE-P4-05: Chapter 31 cleanup

30 records (net −19 from OCR). Removed 19 `-dup` IDs and cross-reference appendix material wrongly captured as entries.

Bootstrap: `python scripts/jsonl_to_module.py --part 4 --chapter N`. OCR: `python scripts/extract_ocr_drafts.py --part 4`.

---

# Part V

Issues discovered when building Part V (Berndt Chapters 32–39, unorganized Notebook II/III + First Notebook). All eight chapters have AI-curated LaTeX in `scripts/entries/p5_chNN.py`.

## Summary counts (Part V)

| Chapter | Title | Records | OCR draft |
|---------|-------|---------|-----------|
| 32 | Continued Fractions (supplement) | 12 | 12 |
| 33 | Elliptic Functions (Alternative Bases) | 2 | 2 |
| 34 | Class Invariants | 199 | 34 |
| 35 | Values of Theta-Functions | 41 | 6 |
| 36 | Modular Equations (supplement) | 82 | 30 |
| 37 | Infinite Series (supplement) | 64 | 16 |
| 38 | Approximations and Asymptotic Expansions | 24 | 17 |
| 39 | Miscellaneous Results (First Notebook) | 20 | 12 |
| **Total** | | **444** | **129** |

Combined dataset: **2352** records — complete Berndt *Ramanujan's Notebooks* Parts I–V.

### ISSUE-P5-01: Part V PDF chapter detection

Same running-header format as Part IV (`32. Continued Fractions`). Reuses `chapter_page_ranges_running_headers(doc, 32, 39)`.

### ISSUE-P5-02: Chapter 33 alternative bases

Only **2 records** (Entry 13.1–13.2 enigmatic formulas on p. 392). Berndt's ~62 count covers the full alternative-base theory in proofs elsewhere; the notebook fragment has few formal headings in this chapter block.

### ISSUE-P5-03: Chapter 34 class invariants

199 records (+165 from OCR). Includes 78 \(G_n\) and 38 \(g_n\) table values as separate records, Entries 2.1–2.2, 8.1–8.5, 11.1–11.21, singular moduli, and decimal sub-IDs (`Entry02-G13`, etc.).

### ISSUE-P5-04: Chapters 35–37 expansion

Ch35: 41 (theta-function values at \(e^{-\pi/n}\)). Ch36: 82 modular equations. Ch37: 64 infinite series including Abel–Plana and theorems 15.1–50.5.

### ISSUE-P5-05: Chapters 38–39

Ch38: 24 approximations (Entries 1–23). Ch39: 20 First Notebook miscellany. Entry 7 in Ch39 reconstructed from proof context where OCR omitted the statement.

Bootstrap: `python scripts/jsonl_to_module.py --part 5 --chapter N`. OCR: `python scripts/extract_ocr_drafts.py --part 5`.
