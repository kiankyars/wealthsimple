"""CHAR TENSOR -- 5x5 word square.
10 clue answers, each placed once: 5 across (rows) and 5 down (columns).
Words may be entered forwards or reversed (see EXAMPLE: DATE fwd, RUIN reversed, ...).
Clues are listed alphabetically so they give no positional information.
Printed circle at r2c4 -> export (letter -> number, A=1..Z=26).
"""
from itertools import permutations

WORDS = ["BADGE","BENCH","CHORE","GLARE","NOMAD","RAMEN","SLATE","TENTH","TERSE","THETA"]

def variants(w):
    return {w, w[::-1]}

def solve():
    sols = []
    n = 5
    # choose which 5 words are rows (as a set), rest are columns
    from itertools import combinations
    for rowset in combinations(range(10), n):
        colset = [i for i in range(10) if i not in rowset]
        # try every assignment of rowset words to rows, in each orientation
        for rowperm in permutations(rowset):
            rowopts = [list(variants(WORDS[i])) for i in rowperm]
            def build(r, grid):
                if r == n:
                    # columns must be the colset words (in some order/orientation)
                    cols = ["".join(grid[i][c] for i in range(n)) for c in range(n)]
                    remaining = list(colset)
                    used = []
                    ok = True
                    for cw in cols:
                        hit = None
                        for idx in remaining:
                            if cw in variants(WORDS[idx]):
                                hit = idx; break
                        if hit is None: ok = False; break
                        remaining.remove(hit); used.append(hit)
                    if ok and not remaining:
                        sols.append([row[:] for row in grid])
                    return
                for opt in rowopts[r]:
                    grid.append(list(opt))
                    # prune: partial columns must be prefixes of some remaining col word
                    good = True
                    for c in range(n):
                        pref = "".join(grid[i][c] for i in range(len(grid)))
                        if not any(any(v.startswith(pref) for v in variants(WORDS[i])) for i in colset):
                            good = False; break
                    if good:
                        build(r+1, grid)
                    grid.pop()
            build(0, [])
    # dedupe (same grid can be reached via different row orders? no, row order fixed by grid)
    uniq = []
    seen = set()
    for g in sols:
        key = tuple("".join(r) for r in g)
        if key not in seen:
            seen.add(key); uniq.append(g)
    return uniq

if __name__ == "__main__":
    sols = solve()
    print("distinct grids:", len(sols))
    for g in sols:
        print()
        for r in g: print("   ", " ".join(r))
        print("    r2c4 (circle) =", g[1][3], "->", ord(g[1][3])-64)
        print("    r4c4          =", g[3][3], "->", ord(g[3][3])-64)
