"""GRADIENT ACCUMULATION  (region 6, the final grid)
9 columns x 4 data rows, plus a column-sum row.
Rules (verified against the printed EXAMPLE, see ga_example_check.py):
  * "First four rows 1-9": every data row is a permutation of 1..9.
  * The 3x3 diagram (8 slashes around a 4) = king-move rule: a value may not repeat
    in any of the 8 cells surrounding it.
  * Bottom row = column sums. Printed for c1,c2,c4,c5,c6,c8,c9; c3 and c7 are BLANK.
Red circle at r1c7 -> the FINAL answer (does not export).
Column-wise DFS with per-row used-digit bitmasks.
"""
from itertools import product

NC, NR = 9, 4
GIVEN = {(1,3):1, (1,6):6, (1,8):4, (1,9):2,
         (2,1):8, (2,2):6,
         (3,6):8,
         (4,1):9, (4,3):5, (4,5):6, (4,9):7}
SUMS = {1:23, 2:15, 4:19, 5:25, 6:19, 8:21, 9:16}
TOTAL = NR * 45

def col_candidates(c, want):
    fixed = {r: GIVEN[(r, c)] for r in range(1, NR+1) if (r, c) in GIVEN}
    rng = [[fixed[r]] if r in fixed else list(range(1, 10)) for r in range(1, NR+1)]
    out = []
    for t in product(*rng):
        if any(t[i] == t[i+1] for i in range(NR-1)):   # vertical king
            continue
        if want is not None and sum(t) != want:
            continue
        out.append(t)
    return out

def diag_ok(prev, cur):
    for i in range(NR):
        if i > 0 and prev[i-1] == cur[i]: return False
        if i < NR-1 and prev[i+1] == cur[i]: return False
    return True

def solve(extra_sums=None, cap=200000):
    sums = dict(SUMS)
    if extra_sums: sums.update(extra_sums)
    blank = [c for c in range(1, NC+1) if c not in sums]
    blank_total = TOTAL - sum(sums.values())
    cands = [col_candidates(c, sums.get(c)) for c in range(1, NC+1)]
    sols = []
    used = [0]*NR
    cur = [None]*NC

    def rec(ci, btot):
        if len(sols) >= cap: return
        if ci == NC:
            if btot == blank_total: sols.append([[cur[c][r] for c in range(NC)] for r in range(NR)])
            return
        c = ci + 1
        isblank = c in blank
        prev = cur[ci-1] if ci else None
        for t in cands[ci]:
            bad = False
            for r in range(NR):
                if used[r] >> t[r] & 1: bad = True; break
            if bad: continue
            if prev is not None and not diag_ok(prev, t): continue
            nb = btot + sum(t) if isblank else btot
            if nb > blank_total: continue
            for r in range(NR): used[r] |= 1 << t[r]
            cur[ci] = t
            rec(ci+1, nb)
            cur[ci] = None
            for r in range(NR): used[r] &= ~(1 << t[r])
    rec(0, 0)
    return sols

def show(s):
    for row in s: print("      " + "  ".join(str(x) for x in row))
    print("      " + "  ".join("%d" % sum(s[i][c] for i in range(NR)) for c in range(NC)) + "   <- column sums")

if __name__ == "__main__":
    base = solve()
    print("solutions from printed data alone:", len(base))
    print("  r1c7 (circled) values:", sorted({s[0][6] for s in base}))
    print("  col3 sums:", sorted({sum(s[i][2] for i in range(NR)) for s in base}))
    print("  col7 sums:", sorted({sum(s[i][6] for i in range(NR)) for s in base}))
    for s in base[:6]:
        print(); show(s)
    print()
    print("--- supplying ONE of the two blank column sums ---")
    for c in (3, 7):
        for v in range(6, 35):
            s = solve({c: v})
            if s:
                print("  col%d = %-3d -> %4d solution(s); r1c7 in %s" %
                      (c, v, len(s), sorted({x[0][6] for x in s})))
