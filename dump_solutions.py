import gradient_flow, residual_connection, char_tensor, dual_param, forward_pass, grad_accum

print("REGION 1 -- GRADIENT FLOW  (export 5)")
s = gradient_flow.solve()[0]
g = [[0]*5 for _ in range(5)]
for (r,c),v in s.items(): g[r-1][c-1]=v
for r in range(5):
    print("   " + " ".join(("(%2d)" % g[r][c]) if (r,c)==(2,3) else (" %2d " % g[r][c]) for c in range(5)))

print("\nREGION 2 -- RESIDUAL CONNECTION  (import 5 at r4c5, export 18)")
sols, grid = residual_connection.solve((3,4), 5)
p = sols[0]; order = {cell:i for i,cell in enumerate(p)}
for r in range(7):
    cells=[]
    for c in range(7):
        v = grid[r][c]
        lab = "START" if v=="S" else ("FIN" if v=="F" else ("--" if v is None else str(v)))
        if (r,c) in order:
            i = order[(r,c)]
            lab = "%s#%d" % (lab, i) if i else lab
            if i == 9: lab = "(" + lab + ")"
        print_cell = lab
        cells.append("%-9s" % print_cell)
    print("   " + "".join(cells))
print("   ('#n' = position in the path; #9 -> the circled square)")

print("\nREGION 3 -- DUAL PARAMETER SPACE  (import 18 -> cell r1c4, export 07 = 7)")
na, nb, ds = dual_param.solve()
a, b = ds[0]
for r in range(5):
    print("   " + " ".join(("(%d%d)" % (a[r][c], b[r][c])) if (r,c)==(3,0)
                           else (" %d%d " % (a[r][c], b[r][c])) for c in range(5)))

print("\nREGION 4 -- CHAR TENSOR  (import 7 = G at r4c1, export h = 8)")
for gr in char_tensor.solve():
    if gr[0] == list("BENCH"):
        for r in range(5):
            print("   " + " ".join(("(%s)" % gr[r][c]) if (r,c)==(1,3) else (" %s " % gr[r][c]) for c in range(5)))

print("\nREGION 5 -- FORWARD PASS  (export = number at r7c3)")
for k, s in enumerate(forward_pass.solve(), 1):
    idx = {cell:i for i,cell in enumerate(s)}
    if forward_pass.CIRCLE not in idx: continue
    print("   candidate path, circled r7c3 = %d, highest number %d" % (idx[forward_pass.CIRCLE], len(s)-2))
    for r in range(1,10):
        row=[]
        for c in range(1,10):
            if (r,c) in idx:
                i=idx[(r,c)]
                t = "STA" if i==0 else ("END" if i==len(s)-1 else str(i))
                if (r,c)==forward_pass.CIRCLE: t="("+t+")"
            else: t="."
            row.append("%5s" % t)
        print("     " + "".join(row))
    print()

print("REGION 6 -- GRADIENT ACCUMULATION  (import 20 -> col7 sum, FINAL ANSWER at r1c7)")
sol = grad_accum.solve({7:20})[0]
for r in range(4):
    print("   " + " ".join(("(%d)" % sol[r][c]) if (r,c)==(0,6) else (" %d " % sol[r][c]) for c in range(9)))
print("   " + " ".join("%3d" % sum(sol[i][c] for i in range(4)) for c in range(9)) + "   <- column sums")
