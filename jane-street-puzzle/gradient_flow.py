"""GRADIENT FLOW (region 1, "Start here") -- 5x5.
"Draw path from 1-25; add numbers and arrows as needed."
EXAMPLE: "Draw path through numbers in order, leaving each square in a straight line in
the direction of 1 of 8 arrows."  So from the cell holding k you travel in a straight
line along that cell's arrow direction and land on the cell holding k+1 (you may pass
over other cells -- verified in the example, 2->3 crosses one cell).
Printed white circle at r3c4 -> export.
"""
import sys
sys.setrecursionlimit(100000)

N = 5
NUM = {(1,4):1, (2,4):25, (3,1):6, (3,3):7, (4,1):17, (4,2):12, (4,5):3}
DIRS = {"N":(-1,0),"S":(1,0),"E":(0,1),"W":(0,-1),
        "NE":(-1,1),"NW":(-1,-1),"SE":(1,1),"SW":(1,-1)}
ARROW = {(1,2):"SW", (1,3):"SW", (1,4):"SE",
         (2,1):"E",  (2,3):"N",  (2,5):"S",
         (3,2):"S",  (3,3):"SE", (3,5):"W",
         (4,1):"S",  (4,2):"E",  (4,3):"SW", (4,4):"SW",
         (5,2):"NW", (5,5):"N"}
CIRCLE = (3,4)
CELLS = [(r,c) for r in range(1,N+1) for c in range(1,N+1)]

def ray(cell, d):
    dr, dc = DIRS[d]; r, c = cell; out = []
    while True:
        r += dr; c += dc
        if not (1 <= r <= N and 1 <= c <= N): return out
        out.append((r,c))

# successors[cell] = set of cells reachable as "next" from cell
SUCC = {}
for cell in CELLS:
    if cell in ARROW:
        SUCC[cell] = set(ray(cell, ARROW[cell]))
    else:
        s = set()
        for d in DIRS: s |= set(ray(cell, d))
        SUCC[cell] = s
# predecessors
PRED = {cell: {o for o in CELLS if cell in SUCC[o]} for cell in CELLS}

FIXED = {v: k for k, v in NUM.items()}   # number -> cell

def solve():
    sols = []
    used = set()
    seq = [None]*(N*N+1)
    def rec(k):
        if k > N*N:
            sols.append(dict(seq_items())); return
        cands = [FIXED[k]] if k in FIXED else None
        if cands is None:
            if k == 1: cands = [c for c in CELLS if c not in used]
            else: cands = [c for c in SUCC[seq[k-1]] if c not in used]
        else:
            if k > 1 and cands[0] not in SUCC[seq[k-1]]: return
            if cands[0] in used: return
        for c in cands:
            if k > 1 and c not in SUCC[seq[k-1]]: continue
            if c in used: continue
            seq[k] = c; used.add(c)
            rec(k+1)
            used.discard(c); seq[k] = None
    def seq_items():
        return [(seq[i], i) for i in range(1, N*N+1)]
    rec(1)
    return sols

if __name__ == "__main__":
    sols = solve()
    print("solutions:", len(sols))
    for s in sols:
        grid = [[0]*N for _ in range(N)]
        for (r,c), v in s.items(): grid[r-1][c-1] = v
        print()
        for row in grid: print("   ", " ".join("%2d" % v for v in row))
        print("    circled cell r3c4 =", grid[CIRCLE[0]-1][CIRCLE[1]-1], " <- EXPORT")
