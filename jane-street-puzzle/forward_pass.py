"""FORWARD PASS  --  9x9 grid.
Path from START (r3c9) to END (r9c6), orthogonal steps, self-avoiding.
Cells are numbered 1..N along the path between START and END.
Given row / column counts = number of path cells in that line (START and END count).
Constraint: no 2x2 block may be entirely occupied by path cells.
Printed circle sits at r7c3 -> the number there is the export.
Rows/cols are 1-indexed; (r, c).
"""
import sys
sys.setrecursionlimit(100000)

N = 9
START = (3, 9)
END = (9, 6)
ROW_CNT = {2: 5, 5: 2, 6: 1, 7: 3}      # printed row labels
COL_CNT = {2: 4, 4: 5, 5: 2, 6: 5, 8: 1}  # printed column labels
CIRCLE = (7, 3)

def solve(row_cnt=ROW_CNT, col_cnt=COL_CNT, limit=200000):
    on = [[False]*(N+2) for _ in range(N+2)]
    rc = [0]*(N+2)
    cc = [0]*(N+2)
    sols = []
    path = []

    def bad_2x2(r, c):
        # after placing (r,c), check the four 2x2 blocks containing it
        for dr in (-1, 0):
            for dc in (-1, 0):
                r0, c0 = r+dr, c+dc
                if 1 <= r0 and r0+1 <= N and 1 <= c0 and c0+1 <= N:
                    if on[r0][c0] and on[r0][c0+1] and on[r0+1][c0] and on[r0+1][c0+1]:
                        return True
        return False

    def feasible():
        # prune: a constrained line already over budget, or impossible to reach budget
        for r, want in row_cnt.items():
            if rc[r] > want:
                return False
        for c, want in col_cnt.items():
            if cc[c] > want:
                return False
        return True

    def rec(r, c):
        if len(sols) > limit:
            return
        on[r][c] = True
        rc[r] += 1
        cc[c] += 1
        path.append((r, c))
        if not bad_2x2(r, c) and feasible():
            if (r, c) == END:
                if all(rc[k] == v for k, v in row_cnt.items()) and \
                   all(cc[k] == v for k, v in col_cnt.items()):
                    sols.append(list(path))
            else:
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 1 <= nr <= N and 1 <= nc <= N and not on[nr][nc]:
                        rec(nr, nc)
        path.pop()
        cc[c] -= 1
        rc[r] -= 1
        on[r][c] = False

    rec(*START)
    return sols

if __name__ == "__main__":
    sols = solve()
    print("solutions:", len(sols))
    for s in sols[:8]:
        # number: START is index 0 (unnumbered), path[1..] are 1..N, END is last
        idx = {cell: i for i, cell in enumerate(s)}
        n_inner = len(s) - 2
        print("  length %d (numbers 1..%d), circle r7c3 = %s" %
              (len(s), n_inner, idx.get(CIRCLE)))
        grid = [["  ." for _ in range(N)] for _ in range(N)]
        for i, (r, c) in enumerate(s):
            lab = "STA" if i == 0 else ("END" if i == len(s)-1 else "%3d" % i)
            grid[r-1][c-1] = lab
        for row in grid:
            print("   ", " ".join(row))
        print()
