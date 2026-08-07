import dual_param as dp, copy, itertools
base_A = [row[:] for row in dp.A]
base_B = [row[:] for row in dp.B]
givens = [("A", r, c) for r in range(5) for c in range(5) if base_A[r][c] is not None] + \
         [("B", r, c) for r in range(5) for c in range(5) if base_B[r][c] is not None]
print("printed digit-slots I read:", len(givens))
def count(remove):
    dp.A = [row[:] for row in base_A]; dp.B = [row[:] for row in base_B]
    for (w, r, c) in remove:
        (dp.A if w == "A" else dp.B)[r][c] = None
    na, nb, sols = dp.solve()
    grids = {tuple(dp.render(a, b)) for a, b in sols}
    return len(grids)
print("all givens ->", count([]), "grid(s)")
print()
print("removing ONE given at a time:")
for g in givens:
    n = count([g])
    print("   drop %s r%dc%d -> %d grid(s)%s" % (g[0], g[1]+1, g[2]+1, n, "   <- essential" if n != 1 else ""))
