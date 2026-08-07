"""Exhaustive proof of the region ordering.

Region 1 = GRADIENT FLOW (printed "#1 / Start here"); region 6 = GRADIENT ACCUMULATION
(the only red circle, matching the cover diagram's terminal grid). That leaves 4! = 24
orderings of the middle four. Test every one against what each sheet can actually accept
and produce.
"""
from itertools import permutations
import gradient_flow, residual_connection as RC, dual_param, char_tensor, forward_pass as FP, grad_accum as GA

# ---------------- what each region can EXPORT, and what it can ACCEPT ----------------
GF_EXPORT = gradient_flow.solve()[0][(3, 4)]                      # 5

# RESIDUAL CONNECTION: an import value is acceptable only if it yields exactly one path
rc_accept = {}
for cell in RC.BLANKS:
    for v in range(1, 22):
        s, g = RC.solve(cell, v)
        if s: rc_accept.setdefault(v, []).append((cell, len(s), g[s[0][9][0]][s[0][9][1]]))
RC_OK = {v: lst[0][2] for v, lst in rc_accept.items() if sum(n for _, n, _ in lst) == 1}

# DUAL PARAMETER SPACE: accepts a two-digit value that is legal and present in its grid
dp_na, dp_nb, dp_s = dual_param.solve()
DP_GRID = [x for line in dual_param.render(*dp_s[0]) for x in line.split()]
DP_EXPORT = int(DP_GRID[15])                                       # r4c1 = 07 -> 7
def dp_accepts(v):
    s = "%02d" % v
    return 0 <= v <= 49 and len(s) == 2 and s[0] in "01234" and s[1] in "56789" and s in DP_GRID

# CHAR TENSOR: accepts value v only if letter(v) pins one of the 8 grids from any cell
ct = char_tensor.solve()
from collections import defaultdict
cells_of = defaultdict(set)
for i, g in enumerate(ct):
    for r in range(5):
        for c in range(5): cells_of[(g[r][c], (r, c))].add(i)
def ct_accepts(v):
    if not 1 <= v <= 26: return False
    ch = chr(64 + v)
    cs = [k[1] for k in cells_of if k[0] == ch]
    return bool(cs) and all(len(cells_of[(ch, c)]) == 1 for c in cs)
CT_EXPORTS = sorted({ord(g[1][3]) - 64 for g in ct})               # {8,12,18,20}

# FORWARD PASS: accepts v only if some invariant that separates its two viable paths
# takes the value v on exactly one of them
fp_paths = [p for p in FP.solve() if FP.CIRCLE in set(p)]
fp_idx = [{c: i for i, c in enumerate(p)} for p in fp_paths]
def fp_facts(p, d):
    """keyed facts: name -> value. A fact separates the paths only if the SAME key takes
    different values on them (so 'number at r1c5' is a different fact from 'number at r4c6')."""
    f = {}
    f["len"] = len(p); f["high"] = len(p)-2; f["off"] = FP.N*FP.N - len(p)
    for r in range(1, FP.N+1): f["row%d" % r] = sum(1 for (rr, _) in p if rr == r)
    for c in range(1, FP.N+1): f["col%d" % c] = sum(1 for (_, cc) in p if cc == c)
    f["block"] = sum(1 for (r, c) in p if 3 <= r <= 7 and 3 <= c <= 7)
    f["tophalf"] = sum(1 for (r, c) in p if r <= 4)
    f["lefthalf"] = sum(1 for (r, c) in p if c <= 4)
    turns = sum(1 for i in range(1, len(p)-1)
                if (p[i][0]-p[i-1][0], p[i][1]-p[i-1][1]) != (p[i+1][0]-p[i][0], p[i+1][1]-p[i][1]))
    f["turns"] = turns; f["runs"] = turns + 1
    for r in range(1, FP.N+1):
        for c in range(1, FP.N+1):
            f["at_r%dc%d" % (r, c)] = d.get((r, c))
    return f
FP_F = [fp_facts(p, d) for p, d in zip(fp_paths, fp_idx)]
FP_CIRC = [d[FP.CIRCLE] for d in fp_idx]
def fp_accepts(v):
    """v is acceptable iff some keyed fact takes value v on exactly one of the two paths.
    Returns the set of circled values that such facts can select."""
    out = set()
    for k in FP_F[0]:
        a, b = FP_F[0][k], FP_F[1][k]
        if a == b: continue
        if a == v: out.add(FP_CIRC[0])
        if b == v: out.add(FP_CIRC[1])
    # the circled cell itself is the export, not the import -- exclude that self-reference
    return out

# GRADIENT ACCUMULATION: accepts a blank column total that makes it unique
GA_OK = {}
for c in (3, 7):
    for v in range(6, 35):
        s = GA.solve({c: v})
        if len(s) == 1: GA_OK[v] = s[0][0][6]

print("what each sheet will accept as its import")
print("  RESIDUAL CONNECTION :", {v: "->%d" % e for v, e in sorted(RC_OK.items())})
print("  DUAL PARAMETER SPACE:", [v for v in range(1, 50) if dp_accepts(v)], "-> %d" % DP_EXPORT)
print("  CHAR TENSOR         :", [v for v in range(1, 27) if ct_accepts(v)], "-> one of", CT_EXPORTS)
print("  FORWARD PASS        :", {v: sorted(fp_accepts(v)) for v in range(1, 40) if fp_accepts(v)})
print("  GRADIENT ACCUMULATION:", {v: "->%d" % e for v, e in sorted(GA_OK.items())}, "(final)")
print()

NAMES = ["RESIDUAL CONNECTION", "DUAL PARAMETER SPACE", "CHAR TENSOR", "FORWARD PASS"]
def step(name, v):
    """returns list of possible exports for `name` given import v, or [] if it can't accept"""
    if name == "RESIDUAL CONNECTION":  return [RC_OK[v]] if v in RC_OK else []
    if name == "DUAL PARAMETER SPACE": return [DP_EXPORT] if dp_accepts(v) else []
    if name == "CHAR TENSOR":          return sorted({ord(ct[i][1][3])-64
                                          for i in range(8)
                                          for cell in [k[1] for k in cells_of if k[0]==chr(64+v)]
                                          if cells_of[(chr(64+v), cell)] == {i}}) if ct_accepts(v) else []
    if name == "FORWARD PASS":         return sorted(fp_accepts(v))
    return []

valid = []
for perm in permutations(NAMES):
    stack = [(0, GF_EXPORT, [])]
    while stack:
        i, val, trace = stack.pop()
        if i == 4:
            if val in GA_OK: valid.append((perm, trace + [("GRADIENT ACCUMULATION", val, GA_OK[val])]))
            continue
        for out in step(perm[i], val):
            stack.append((i+1, out, trace + [(perm[i], val, out)]))

print("orderings of the middle four that survive every constraint: %d of 24" % len({v[0] for v in valid}))
print()
seen = set()
for perm, trace in valid:
    if perm in seen: continue
    seen.add(perm)
    print("  ORDER: 1 GRADIENT FLOW -> " + " -> ".join("%d %s" % (i+2, n) for i, n in enumerate(perm)) + " -> 6 GRADIENT ACCUMULATION")
finals = {trace[-1][2] for _, trace in valid}
print()
print("distinct chains found: %d" % len(valid))
for perm, trace in valid:
    print("   " + "  ".join("%s=%d" % (n.split()[0][:4], o) for n, v, o in trace))
print()
print("FINAL ANSWER over every surviving chain:", finals)
