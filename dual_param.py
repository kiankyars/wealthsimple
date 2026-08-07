"""DUAL PARAMETER SPACE -- 5x5, each cell a two-digit number "ab".
"0-4 then 5-9 -- no repeated digit in any row or column, and two-digit numbers do not repeat."
=> a is a Latin square on {0,1,2,3,4}, b is a Latin square on {5,6,7,8,9},
   and the 25 (a,b) pairs are all distinct  (a Graeco-Latin / Euler square).
Printed circle at r4c1 -> export.
Printed givens read off the sheet: '.' = blank slot printed as an underscore.
"""
import sys
# first-digit givens (0-4) and second-digit givens (5-9); None = blank
A = [[None, 4,   0,   None, None],
     [None, 1,   4,   None, 0   ],
     [None, None,None,None, None],
     [0,    None,None,3,    None],
     [4,    3,   None,None, None]]
B = [[None, None,6,   None, 7   ],
     [None, None,5,   None, None],
     [None, 5,   8,   None, None],
     [None, 8,   None,5,    None],
     [None, None,None,9,    None]]
N = 5
FIRST = [0,1,2,3,4]
SECOND = [5,6,7,8,9]

def latin_solutions(given, symbols, extra=None):
    """all Latin squares matching `given` (list of lists with None)."""
    g = [row[:] for row in given]
    if extra:
        for (r, c), v in extra.items(): g[r][c] = v
    sols = []
    def rec(pos):
        if pos == N*N:
            sols.append([row[:] for row in g]); return
        r, c = divmod(pos, N)
        if g[r][c] is not None:
            v = g[r][c]
            if v in (g[r][x] for x in range(c)) or v in (g[y][c] for y in range(r)): return
            rec(pos+1); return
        for v in symbols:
            if any(g[r][x] == v for x in range(N)): continue
            if any(g[y][c] == v for y in range(N)): continue
            g[r][c] = v
            rec(pos+1)
            g[r][c] = None
    rec(0)
    return sols

def solve(extraA=None, extraB=None):
    As = latin_solutions(A, FIRST, extraA)
    Bs = latin_solutions(B, SECOND, extraB)
    out = []
    for a in As:
        for b in Bs:
            pairs = {(a[r][c], b[r][c]) for r in range(N) for c in range(N)}
            if len(pairs) == 25:
                out.append((a, b))
    return len(As), len(Bs), out

def render(a, b):
    return ["  ".join("%d%d" % (a[r][c], b[r][c]) for c in range(N)) for r in range(N)]

if __name__ == "__main__":
    na, nb, sols = solve()
    print("first-digit Latin squares matching print :", na)
    print("second-digit Latin squares matching print:", nb)
    print("orthogonal (valid) combinations           :", len(sols))
    seen = set()
    for a, b in sols:
        key = tuple(render(a, b))
        if key in seen: continue
        seen.add(key)
    print("distinct grids:", len(seen))
    for k in sorted(seen)[:12]:
        print()
        for line in k: print("   ", line)
        print("    r4c1 (circle) =", k[3].split()[0])
