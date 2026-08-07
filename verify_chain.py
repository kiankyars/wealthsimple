"""End-to-end verification of the whole six-region chain."""
import gradient_flow, residual_connection, char_tensor, dual_param, forward_pass, grad_accum

L = lambda n: chr(64+n)
ok = lambda b: "OK " if b else "FAIL"
print("="*72)
print("REGION 1  GRADIENT FLOW   (printed '#1', 'Start here' - no import)")
s = gradient_flow.solve()
print("  solutions:", len(s), ok(len(s) == 1))
g1 = [[0]*5 for _ in range(5)]
for (r, c), v in s[0].items(): g1[r-1][c-1] = v
for row in g1: print("     ", " ".join("%2d" % v for v in row))
e1 = g1[2][3]
print("  circled r3c4 =", e1, "-> EXPORT")

print("="*72)
print("REGION 2  RESIDUAL CONNECTION  (imports %d)" % e1)
none, _ = residual_connection.solve()
print("  solutions with no import:", len(none), ok(len(none) == 0), "(so an import is required)")
tot = {}
for cell in residual_connection.BLANKS:
    for v in range(1, 22):
        sl, gr = residual_connection.solve(cell, v)
        if sl: tot.setdefault(v, []).append((cell, len(sl)))
uniq_vals = sorted(v for v, lst in tot.items() if sum(n for _, n in lst) == 1)
print("  import values giving exactly ONE solution overall:", uniq_vals)
print("  -> %d is among them: %s" % (e1, ok(e1 in uniq_vals)))
cell = tot[e1][0][0]
sols, grid = residual_connection.solve(cell, e1)
p = sols[0]
print("  import cell = r%dc%d" % (cell[0]+1, cell[1]+1))
print("  path values:", [grid[r][c] for r, c in p[1:-1]])
e2 = grid[p[9][0]][p[9][1]]
print("  9th square (excluding START) =", e2, "-> EXPORT")

print("="*72)
print("REGION 3  DUAL PARAMETER SPACE  (imports %d as the two-digit cell '%02d')" % (e2, e2))
na, nb, ds = dual_param.solve()
grids = {tuple(dual_param.render(a, b)) for a, b in ds}
print("  solutions:", len(grids), ok(len(grids) == 1))
dg = sorted(grids)[0]
for line in dg: print("     ", line)
cells = [x for line in dg for x in line.split()]
tgt = "%02d" % e2
if tgt in cells:
    i = cells.index(tgt)
    print("  cell '%s' appears in the solved grid at r%dc%d: %s" % (tgt, i//5+1, i%5+1, ok(True)))
else:
    print("  cell '%s' does NOT appear in the solved grid: %s" % (tgt, ok(False)))
e3 = int(dg[3].split()[0])
print("  circled r4c1 = %02d -> EXPORT %d" % (e3, e3))

print("="*72)
print("REGION 4  CHAR TENSOR  (imports %d = letter %s)" % (e3, L(e3)))
cs = char_tensor.solve()
print("  grids consistent with the 10 clue answers:", len(cs), "(the 8 dihedral images)")
# a letter fixes the orientation iff its 8 dihedral images sit in 8 DISTINCT cells
from collections import defaultdict
places = defaultdict(set)
for i, g in enumerate(cs):
    for r in range(5):
        for c in range(5):
            places[g[r][c]].add((r, c))
once = sorted(ch for ch, st in places.items() if len(st) == 8)
print("  letters whose 8 placements are all distinct (so a single one fixes the grid):", once)
print("  -> imported letter %s is one of them: %s" % (L(e3), ok(L(e3) in once)))
print("  each placement of %s selects one grid; circled r2c4 value per placement:" % L(e3))
for i, g in enumerate(cs):
    pos = [(r+1, c+1) for r in range(5) for c in range(5) if g[r][c] == L(e3)]
    print("     %s at r%dc%d -> circle r2c4 = %s = %d" %
          (L(e3), pos[0][0], pos[0][1], g[1][3], ord(g[1][3])-64))

print("="*72)
print("REGION 5  FORWARD PASS")
fs = forward_pass.solve()
viable = [x for x in fs if forward_pass.CIRCLE in set(x)]
vals = sorted({{c: i for i, c in enumerate(x)}[forward_pass.CIRCLE] for x in viable})
print("  solutions matching the printed counts:", len(fs))
print("  ... of which have a number at the printed circle r7c3:", len(viable))
print("  possible circled values -> EXPORT:", vals)

print("="*72)
print("REGION 6  GRADIENT ACCUMULATION  (final - circle does not export)")
base = grad_accum.solve()
print("  solutions from printed data alone:", len(base))
print("  r1c7 across them:", sorted({x[0][6] for x in base}))
uniq = {}
for c in (3, 7):
    for v in range(6, 35):
        s = grad_accum.solve({c: v})
        if len(s) == 1: uniq[(c, v)] = s[0][0][6]
print("  blank column sums that yield a UNIQUE grid:")
for (c, v), ans in sorted(uniq.items()):
    print("     col%d = %-3d -> unique, r1c7 = %d" % (c, v, ans))
print("  FORWARD PASS can export %s; those that uniquely solve this grid:" % vals)
good = [(c, v) for (c, v) in uniq if v in vals]
for c, v in sorted(good):
    print("     export %d -> col%d -> r1c7 = %d" % (v, c, uniq[(c, v)]))
finals = {uniq[k] for k in good}
print()
print("  FINAL ANSWER (red circle, r1c7):", finals, ok(len(finals) == 1))
sol = grad_accum.solve({good[0][0]: good[0][1]})[0]
print()
grad_accum.show(sol)
