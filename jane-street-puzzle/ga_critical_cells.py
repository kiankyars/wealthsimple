"""Which cells, if I mis-read a PRINTED given as pencil, would change the answer?"""
import grad_accum as ga
grids = ga.solve()
grids.sort(key=lambda g: tuple(tuple(r) for r in g))
lab = {}
for i, g in enumerate(grids, 1): lab[i] = g
print("grid r1c7 values:", {i: g[0][6] for i, g in lab.items()})
print()
print("cells where the three grids DISAGREE (a printed given here would decide it):")
print()
print("  cell    grid1  grid2  grid3   decides")
crit8, crit9 = [], []
for r in range(4):
    for c in range(9):
        vs = [lab[i][r][c] for i in (1, 2, 3)]
        if len(set(vs)) == 1: continue
        who = {}
        for v in set(vs):
            keep = [i for i in (1,2,3) if lab[i][r][c] == v]
            who[v] = keep
        dec = []
        for v, keep in sorted(who.items()):
            ans = sorted({lab[i][0][6] for i in keep})
            dec.append("%d->grids%s r1c7%s" % (v, keep, ans))
            if len(keep) == 1 and lab[keep[0]][0][6] == 8: crit8.append((r+1, c+1, v))
        star = " *" if (r+1, c+1) in [(x[0], x[1]) for x in crit8] else ""
        print("  r%dc%d     %d      %d      %d    %s%s" % (r+1, c+1, vs[0], vs[1], vs[2], "; ".join(dec), star))
print()
print("The ONLY (cell, value) facts that would force r1c7 = 8:")
for r, c, v in crit8:
    print("   r%dc%d = %d   (pencil on the sheet says %d)" % (r, c, v, lab[1][r-1][c-1]))
print()
print("=> these are the cells to re-check on the photograph. If none of them is a")
print("   printed given, the answer cannot be 8.")
