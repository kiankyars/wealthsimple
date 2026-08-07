"""Which single (cell, letter) fact fixes CHAR TENSOR's orientation?
The clue answers admit 8 grids (the dihedral images of one word square), so exactly one
extra letter is needed. A value V imported as letter L is USABLE only if every cell where
L can sit belongs to just one of the 8 grids."""
import char_tensor as ct
from collections import defaultdict

sols = ct.solve()
print("grids consistent with the 10 clue answers:", len(sols))
match = defaultdict(list)                      # (cell, letter) -> grid indices
for i, g in enumerate(sols):
    for r in range(5):
        for c in range(5):
            match[((r+1, c+1), g[r][c])].append(i)

print("\nletter  per-grid count  cells it can occupy  worst-case #grids left")
rows = []
for ch in sorted({c for g in sols for row in g for c in row}):
    per = sum(row.count(ch) for row in sols[0])
    cells = sorted({cell for (cell, l) in match if l == ch})
    worst = max(len(match[(cell, ch)]) for cell in cells)
    rows.append((ch, per, len(cells), worst))
for ch, per, ncell, worst in rows:
    flag = "  <-- pins the grid" if worst == 1 else ""
    print("  %s (=%2d)      %d            %2d                   %d%s"
          % (ch, ord(ch)-64, per, ncell, worst, flag))

usable = [ch for ch, per, n, w in rows if w == 1]
print("\nletters that pin the grid from a single cell:", usable)
print("as numbers:", sorted(ord(c)-64 for c in usable))
print()
for v in (5, 7, 8, 12, 18, 20, 22):
    ch = chr(64+v) if 1 <= v <= 26 else "?"
    print("  import %2d = %-2s -> %s" % (v, ch,
          "USABLE (fixes the grid)" if ch in usable else "NOT usable (leaves >1 grid)"))
print()
print("detail for R (=18), the value REGION 2 exports:")
for cell in sorted({cell for (cell, l) in match if l == "R"}):
    print("   R at r%dc%d -> matches grid(s) %s" % (cell[0], cell[1],
          [i+1 for i in match[(cell, "R")]]))
print()
print("detail for G (=7), the value DUAL PARAMETER SPACE exports:")
for cell in sorted({cell for (cell, l) in match if l == "G"}):
    i = match[(cell, "G")][0]
    print("   G at r%dc%d -> grid %d, circled r2c4 = %s = %d"
          % (cell[0], cell[1], i+1, sols[i][1][3], ord(sols[i][1][3])-64))
