import forward_pass as fp

N = fp.N
def counts(path):
    rc = [0]*(N+1); cc = [0]*(N+1)
    for r, c in path: rc[r] += 1; cc[c] += 1
    return rc, cc

def self_touching(path):
    idx = {cell: i for i, cell in enumerate(path)}
    bad = []
    for i, (r, c) in enumerate(path):
        for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            j = idx.get((nr, nc))
            if j is not None and abs(i-j) > 1:
                bad.append(((r,c),(nr,nc)))
    return bad

sols = fp.solve()
print("raw solutions matching the printed row/column counts:", len(sols))
for k, s in enumerate(sols, 1):
    idx = {cell: i for i, cell in enumerate(s)}
    circ = idx.get(fp.CIRCLE)
    rc, cc = counts(s)
    st = self_touching(s)
    print("\n--- solution %d ---" % k)
    print("  cells=%d  highest number=%d" % (len(s), len(s)-2))
    print("  number at printed circle r7c3: %s" % (circ if circ else "NOT ON PATH"))
    print("  row counts:", rc[1:], "   (printed: r2=5 r5=2 r6=1 r7=3)")
    print("  col counts:", cc[1:], "   (printed: c2=4 c4=5 c5=2 c6=5 c8=1)")
    print("  self-touching (non-consecutive orthogonal contacts): %d %s"
          % (len(st)//2, [p for p in st[:6]]))

viable = [s for s in sols if fp.CIRCLE in set(s)]
print("\nsolutions with a number at the circled cell:", len(viable))
print("their circle values:", [ {c:i for i,c in enumerate(s)}[fp.CIRCLE] for s in viable ])
nontouch = [s for s in viable if not self_touching(s)]
print("of those, non-self-touching:", len(nontouch),
      "-> circle values", [ {c:i for i,c in enumerate(s)}[fp.CIRCLE] for s in nontouch ])

# what single extra line-count would separate the viable solutions?
print("\nline counts that differ between the viable solutions:")
cs = [counts(s) for s in viable]
for r in range(1, N+1):
    vals = [c[0][r] for c in cs]
    if len(set(vals)) > 1 and r not in fp.ROW_CNT: print("   row %d : %s" % (r, vals))
for c in range(1, N+1):
    vals = [x[1][c] for x in cs]
    if len(set(vals)) > 1 and c not in fp.COL_CNT: print("   col %d : %s" % (c, vals))
