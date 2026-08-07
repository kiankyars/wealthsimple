"""RESIDUAL CONNECTION  --  7x7 grid.
"Start to finish, no diagonal moves, include each number exactly once,
 avoid blanks except where a number has been imported from another grid."
START = r1c1, FINISH = r7c7.  Values 1..21 each appear one or more times in the grid;
the path must contain exactly one cell of each value, and must not enter a blank cell
except the single blank that holds the imported number.
"When finished, circle the ninth square in the path (not including START)" -> export.
"""
import sys
sys.setrecursionlimit(100000)

B = None   # blank
GRID = [
    ["S", 14, 15,  4, 13,  3,  B],
    [ 16,  4, 20, 21, 18,  B,  8],
    [  3, 17, 11, 10,  6,  B,  1],
    [ 10, 14,  B,  9,  B, 16, 17],
    [ 18,  B,  7,  2, 12,  6, 21],
    [  2,  B,  8, 11, 15,  9, 13],
    [  B,  7, 19,  1, 12,  5, "F"],
]
N = 7
START, FINISH = (0, 0), (6, 6)
VALUES = sorted({v for row in GRID for v in row if isinstance(v, int)})
BLANKS = [(r, c) for r in range(N) for c in range(N) if GRID[r][c] is B]

def solve(import_cell=None, import_val=None, cap=50):
    """import_cell: (r,c) blank that receives import_val. None = no import allowed."""
    grid = [row[:] for row in GRID]
    if import_cell is not None:
        r, c = import_cell
        assert grid[r][c] is B
        grid[r][c] = import_val
    target = set(VALUES)
    if import_val is not None and import_val not in target:
        target.add(import_val)
    sols = []
    seen = [[False]*N for _ in range(N)]

    def rec(r, c, have, path):
        if len(sols) >= cap: return
        if (r, c) == FINISH:
            if have == target:
                sols.append(list(path))
            return
        for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if not (0 <= nr < N and 0 <= nc < N) or seen[nr][nc]: continue
            v = grid[nr][nc]
            if v is B: continue
            if v == "S": continue
            if v == "F":
                seen[nr][nc] = True; path.append((nr,nc))
                rec(nr, nc, have, path)
                path.pop(); seen[nr][nc] = False
                continue
            if v in have: continue
            if import_cell is not None and (nr,nc) != import_cell and grid[nr][nc] is not B:
                pass
            seen[nr][nc] = True; path.append((nr,nc)); have.add(v)
            rec(nr, nc, have, path)
            have.discard(v); path.pop(); seen[nr][nc] = False

    seen[0][0] = True
    rec(0, 0, set(), [START])
    return sols, grid

def ninth(path):
    # path[0] is START; the 9th square not including START is path[9]
    return path[9] if len(path) > 9 else None

if __name__ == "__main__":
    print("values present in the printed grid:", VALUES)
    print("blank cells (0-indexed):", BLANKS)
    print()
    s, _ = solve()
    print("solutions with NO import (blanks all forbidden):", len(s))
    print()
    print("--- one blank filled with an imported value ---")
    for cell in BLANKS:
        for val in range(1, 22):
            sols, grid = solve(cell, val)
            if sols:
                nin = {grid[r][c] for r, c in (ninth(p) for p in sols) if True}
                print("  blank r%dc%d <- %-2d : %2d solution(s); 9th square value(s) = %s"
                      % (cell[0]+1, cell[1]+1, val, len(sols), sorted(nin)))
