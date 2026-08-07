# Jane Street "Traverse the Parameter Space"

Six ML-themed grid puzzles on punch-card sheets, plus a purple cover sheet.

> Your neural network is stuck. … You've mapped the terrain into six interconnected
> optimization regions, each a grid that will solve uniquely to reveal a critical
> parameter. You know where to begin your descent, but the other five regions are
> presented in random order: figuring out the correct sequence is part of the challenge.
> … Solving one region will give you information needed for the next.
> *(Final circled number does not export.)*

## Status

**The six grids are solved and verified. The final circled parameter is 9 — but that is not
what the kiosk accepts.** The submission page at
[parameterspace.wondermakr.com/en/answer](https://parameterspace.wondermakr.com/en/answer)
takes *text* (max 25 chars) under the heading:

> Use this phrase to arrive at your final answer:
> **Voyages Nearing Zero Descend**

So the six circled parameters — **5, 18, 7, 8, 20, 9** — feed one more decoding step, which
is still open. See [The final decode](#the-final-decode) at the end.

## Mechanics

Every sheet carries a pre-printed **white circle** in one cell — the value there is that
region's **export**. The exported number is the missing datum the *next* region needs.
The cover's chain diagram shows six grids left→right, each white circle feeding the next
grid's red import triangle; the last grid's circle is **red** and does not export.

Only **GRADIENT ACCUMULATION** has a red circle → it is region 6.
Only **GRADIENT FLOW** is printed "#1 / Start here" → region 1.

## The chain

| # | Region | Import | Export |
|---|--------|--------|--------|
| 1 | GRADIENT FLOW | — (start) | **5** (r3c4) |
| 2 | RESIDUAL CONNECTION | 5 → blank cell r4c5 | **18** (9th square in the path) |
| 3 | DUAL PARAMETER SPACE | 18 → cell r1c4 | **07** (r4c1) → 7 |
| 4 | CHAR TENSOR | 7 = **G** (A=1…Z=26) | **h** (r2c4) → 8 |
| 5 | FORWARD PASS | 8 | **20** (r7c3) |
| 6 | GRADIENT ACCUMULATION | 20 → blank col-7 sum | **9** (r1c7) — final parameter, does not export |

## The ordering, proved by exhaustive search

`prove_ordering.py` fixes region 1 (printed "#1 / Start here") and region 6 (the only red
circle) and tries all **4! = 24** orderings of the middle four, checking each against what
every sheet will actually accept and produce. **Exactly one of the 24 survives** — the one
above. Each sheet's acceptance set, computed from its own solver:

| Region | will accept as import | then exports |
|---|---|---|
| RESIDUAL CONNECTION | **5** or 6 (nothing else gives a unique path) | 18, or 4 |
| DUAL PARAMETER SPACE | any legal `ab` value in its grid — 18 among them | 7 |
| CHAR TENSOR | only **3, 7, 19** (= C, G, S — the only letters that pin the orientation) | 8, 12, 18 or 20 |
| FORWARD PASS | anything that separates its two paths | 20 or 22 |
| GRADIENT ACCUMULATION | only **20** or **22** | 9 — final |

The chain of eliminations that leaves one ordering:

* Nothing in the puzzle produces 5 or 6 except region 1, and RESIDUAL CONNECTION accepts
  nothing else → it must be **region 2**, and exports 18.
* FORWARD PASS cannot be region 3: it would export 20 or 22, and neither DUAL PARAMETER
  SPACE (`20`, `22` are not legal cells) nor CHAR TENSOR (accepts only 3, 7, 19) could take
  it → region 3 is **DUAL PARAMETER SPACE**, exporting 7.
* FORWARD PASS cannot be region 4 either, for the same reason — CHAR TENSOR could not accept
  its 20 or 22 → region 4 is **CHAR TENSOR**, region 5 is **FORWARD PASS**.
* No invariant of FORWARD PASS's two paths equals 7, which independently rules it out of
  slot 4 (`fp_invariants.py`).

Eight chains remain overall — CHAR TENSOR's export depends on which cell the G lands in
(8, 12, 18 or 20) and FORWARD PASS's on which of its two paths is intended (20 or 22). **All
eight end at 9.**

## How the ordering is forced

* **Region 1** is printed on the sheet ("#1", "Start here"). Its grid is uniquely
  solvable with no import → exports 5.
* **Region 2 = RESIDUAL CONNECTION.** It has **zero** solutions if no blank is used, so an
  import is mandatory. Sweeping all 8 blanks × all values 1–21, only **5** and **6** give
  exactly one solution overall. Nothing in the puzzle exports 6, so it imports 5 → region 2.
* **Region 6 = GRADIENT ACCUMULATION** (only red circle). Its printed data leaves 3
  solutions; supplying one of the two blank column sums makes it unique only for
  **col7 = 20** or **col3 = 22**.
* **Region 5 = FORWARD PASS.** Its printed row/column counts leave 3 paths, 2 of which put
  a number in the printed circle — with values **exactly {20, 22}**, the only two values
  that uniquely solve region 6. So FORWARD PASS feeds GRADIENT ACCUMULATION.
* **Regions 3 and 4.** The clue answers alone leave CHAR TENSOR with 8 grids (the dihedral
  images of one word square), so one letter must fix the orientation. Only **C(3), G(7),
  S(19)** do — every other letter leaves ≥2 grids. Region 2 exports **18 = R**, and R sits
  at the same cell in two different grids, so CHAR TENSOR *cannot* be region 3. But 18 is a
  legal DUAL PARAMETER SPACE cell value, and DUAL PARAMETER SPACE exports 07 → **7 = G**,
  which does fix CHAR TENSOR. Hence 3 = DUAL PARAMETER SPACE, 4 = CHAR TENSOR.

## Per-region rules (deduced from each sheet's EXAMPLE box)

* **GRADIENT FLOW** — place 1…25; from the cell holding *k* travel in a straight line along
  that cell's arrow (1 of 8 directions) to land on *k+1*, passing over cells freely.
* **RESIDUAL CONNECTION** — START→FINISH, orthogonal steps, include each value 1…21 exactly
  once, never enter a blank except the one holding the imported number. Circle the 9th
  square (START not counted).
* **DUAL PARAMETER SPACE** — every cell is "ab" with a ∈ 0–4 and b ∈ 5–9; a and b each form
  a Latin square and all 25 pairs are distinct (a 5×5 Graeco-Latin / Euler square).
* **CHAR TENSOR** — 5×5 double word square; all 5 rows and all 5 columns are clue answers,
  each usable forwards **or reversed** (the example does exactly this). A=1…Z=26 converts
  on import and export.
* **FORWARD PASS** — START→END orthogonal self-avoiding path numbered 1,2,3,…; the printed
  edge numbers count path cells in that row/column (START and END count); no 2×2 block may
  be fully occupied.
* **GRADIENT ACCUMULATION** — each of the 4 rows is a permutation of 1–9; bottom row gives
  column sums; the little 3×3 diagram (8 slashes around a "4") is a **king-move** rule — a
  value may not repeat in any of the 8 surrounding cells. Verified against the printed
  example in `ga_example_check.py`.

## Solutions

```
REGION 1  GRADIENT FLOW                REGION 3  DUAL PARAMETER SPACE
  19  20  23   1   9                     25  49  06  18  37     <- 18 imported at r1c4
  21  24  22  25   2                     39  17  45  26  08
   6  11   7  (5) 10   <- export 5       16  05  38  47  29
  17  12  15  13   3                    (07) 28  19  35  46     <- export 07 = 7
  18  16  14   4   8                     48  36  27  09  15

REGION 2  RESIDUAL CONNECTION          REGION 4  CHAR TENSOR
 path: START 16 3 10 14 17 4 20 21       B  E  N  C  H
       (18) 6 [5] 12 2 7 8 19 1          A  T  E (H) T   <- export h = 8
       11 15 9 13 FINISH                 D  A  M  O  N
 [5] = imported number in the blank      G  L  A  R  E   <- G = 7 imported at r4c1
 at r4c5;  (18) = 9th square             E  S  R  E  T
                                         rows  BENCH THETA< NOMAD< GLARE TERSE<
                                         cols  BADGE SLATE< RAMEN< CHORE TENTH<
                                         ("<" = entered reversed)

REGION 5  FORWARD PASS                 REGION 6  GRADIENT ACCUMULATION
  .  .  .  9  8  7  .  .  .              5  3  1  7  8  6 (9) 4  2   <- final parameter 9
 13 12 11 10  .  6  .  .  .              8  6  9  5  2  4  3  7  1
 14  .  .  .  .  5  .  . STA             1  4  7  3  9  8  5  2  6
 15  .  .  .  .  4  3  2  1              9  2  5  4  6  1  3  8  7
 16 17  .  .  .  .  .  .  .             23 15 22 19 25 19 20 21 16   <- col sums
  . 18  .  .  .  .  .  .  .                    ^^          ^^
  . 19 (20) 21 .  .  .  .  .             col3 = 22 and col7 = 20 are blank on the sheet;
  .  .  . 22  .  .  .  .  .              supplying either one makes the grid unique.
  .  .  . 23 24 END .  .  .
      (20) = export
```

## Scripts

| file | what it does |
|---|---|
| `gradient_flow.py` | region 1 — arrow-path solver. **1** solution |
| `residual_connection.py` | region 2 — path solver; sweeps every blank × value |
| `dual_param.py` | region 3 — Graeco-Latin square solver. **1** solution |
| `dp_sensitivity.py` | how redundant region 3's printed givens are |
| `char_tensor.py` | region 4 — double word square. **8** grids from clues alone |
| `ct_disambig.py` | which single letter fixes the orientation (only C, G, S) |
| `forward_pass.py` | region 5 — counted path solver. **3** paths, 2 viable |
| `fp_analysis.py` | analysis of what separates the region 5 candidates |
| `grad_accum.py` | region 6 — column-wise solver with the king rule |
| `ga_example_check.py` | proves the rule set against the printed example |
| `verify_chain.py` | walks the whole chain end to end |
| `verify_final_grid.py` | independent re-check of the region 6 answer grid |
| `ga_robustness.py` | region 6 re-derived by a second algorithm; every possible extra fact swept |
| `ga_critical_cells.py` | the only six cells whose printing could change the answer |
| `independent_checks.py` | all three path puzzles re-solved searching from the far end |
| `fp_invariants.py` | 108 candidate invariants of region 5's two paths; which could be its import |
| `prove_ordering.py` | brute-forces all 24 orderings of regions 2-5; exactly one survives |
| `dump_solutions.py` | prints all six solved grids |
| `decode_phrase.py` | tries every extraction scheme against the kiosk phrase |
| `solve_phrase.py` | anchors on the two certain parameters and hunts spellable words |

`decode_phrase.py` and `solve_phrase.py` need a word list at `/tmp/words.txt`:

```sh
pip install english-words
python3 -c "from english_words import get_english_words_set as g; \
open('/tmp/words.txt','w').write('\n'.join(sorted(g(['web2'], lower=True))))"
```

## Confidence in region 6 (the sheet the annotations were least sure about)

Two solvers using completely different algorithms — one column-wise with bitmask row
tracking, one enumerating rows 1 and 4 then pairing rows 2/3 column by column — return the
**same 3 grids** from the printed data (`ga_robustness.py`):

| grid | r1c7 | blank totals |
|---|---|---|
| A | **9** | col3 = 18, col7 = 24 — *this is the pencil grid on the sheet* |
| B | **9** | col3 = 22, col7 = 20 — *the one the import selects* |
| C | 8 | col3 = 18, col7 = 24 |

Three things make **9** safe:

1. The pencil grid on the sheet is genuinely valid — it satisfies every printed cell, every
   printed total, the row permutations and the king rule. It just isn't the *only* grid that
   does. It reads **9**.
2. Grid C is the only one reading 8, and it shares its blank totals (18 / 24) with grid A —
   so **no column-total import can ever isolate it**. An import of 18 leaves 8 and 9 both
   open; only 22 (col 3) or 20 (col 7) give a unique grid, and both give grid B → **9**.
3. Forcing 8 would need a *printed cell* given at one of exactly six positions —
   r1c5 = 9, r1c7 = 8, r2c5 = 1, r2c6 = 2, r4c6 = 3, r4c7 = 4 (`ga_critical_cells.py`).
   Every one of those cells was re-examined at maximum magnification against a
   printed-ink-only threshold: all six are graphite, none is printed. The only machine-set
   digits anywhere near them are the `6`s at r1c6 and r4c5, and r1c7 holds nothing but the
   printed red ring.

So the answer is 9 whether you trust the pencil grid or the uniquely-forced one — and the
one reading 8 is unreachable.

### Independent reverse-direction checks

`independent_checks.py` re-solves the three path puzzles searching from the far end with a
different move order and different pruning:

* GRADIENT FLOW numbered 25 → 1: **1** solution, identical grid, circle = 5
* RESIDUAL CONNECTION from FINISH → START: 34 solutions across all (blank, value) pairs,
  matching the forward search exactly; import 5 gives the same single path, 9th square = 18
* FORWARD PASS from END → START: the **same 3** paths, 2 with a number at the circle, values {20, 22}

## One loose end (does not affect the answer)

FORWARD PASS's printed data (5 column counts, 4 row counts, START, END) leaves **two**
valid paths, circling **20** and **22**. Nothing printed on that sheet identifies where its
import goes — there is no blank count slot, no marked cell, and no pre-shaded cell
(checked by measuring every cell's printed background). The two candidates differ only in
the counts for rows 1/3/4 and columns 3/9, none of which equals any value available in the
chain, so the import mechanism there stays unidentified.

It does not matter: **20** lands in region 6's blank col-7 sum and **22** in its blank col-3
sum, and *both* pick out the same region 6 grid — whose red-circled cell is **9**.

## The final decode

The kiosk is a physical installation: idle attract video → tap → `/en/answer` →
`POST /en/ajax {command: check_answer}` → correct/incorrect → prize link. Validation is
server-side, so there is no answer to read out of the client.

The phrase is **"Voyages Nearing Zero Descend"** — 4 words, **25 letters**, and the input's
`maxlength` is exactly 25.

Ruled out, with reasons:

* **The parameters are not letter-positions in the phrase.** Regions 1–3 are certain
  (5, 18, 7), forcing the first three letters to `g o s` (1-based), `e D N` (0-based) or
  `g e s` (counting spaces). Nothing continues any of those given the constrained values for
  regions 4–6 — `gosh` is the only candidate and the phrase has no **h**.
* **The answer is not spelled from the phrase's letters at all** — it contains no **H** and
  no **T**, so EIGHT, RIGHT, HEIGHT, DESCENT and GRADIENT are unspellable from it.
* **A=1…Z=26** on the six parameters gives **E R G H T I**. No 6-letter anagram exists; the
  5-letter subsets are EIGHT, RIGHT, TIGER, THEIR, GIRTH, GRITH, TIGRE, ITHER.

About 50 candidates were checked against the site's own endpoint — every ordering and
separator of the six numbers, all the anagram words above, ascending/descending readings of
"Nearing Zero Descend" as sort instructions, sums, the initials `VNZD`, and thematic words
(converge, convergence, gradient descent, global minimum, parameter space, landing, height,
descent, minimum, altitude, …). All rejected.

**Most likely missing piece: the punch-hole strips.** Every sheet carries a strip of
fixed-pitch positions along one edge, each either physically **cut**, printed as a **pale
square**, plain, or the printed **circle** (red on GRADIENT ACCUMULATION, white elsewhere,
at a different position on each sheet). That is a Cardan grille, and it is the only decoder
on the cards that none of the grid puzzles uses.

Testable prediction: **stack the six sheets in the solved order** — GRADIENT FLOW, RESIDUAL
CONNECTION, DUAL PARAMETER SPACE, CHAR TENSOR, FORWARD PASS, GRADIENT ACCUMULATION — and see
which strip positions stay open through all six, then read those positions off the 25-letter
phrase. The strip pitch measures ~20–25 positions, consistent with a 25-letter phrase, but
the available photographs are too oblique to classify each position reliably.
