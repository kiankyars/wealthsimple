"""FORWARD PASS has two viable paths (circling 20 and 22). Its import must be a single
fact that separates them. Enumerate a broad family of candidate facts and test which ones
differ, then check those against the values the chain can actually deliver."""
import forward_pass as fp
N = fp.N
CHAIN = {5:"GRADIENT FLOW", 7:"DUAL PARAMETER SPACE (07)", 8:"CHAR TENSOR (h)",
         12:"CHAR TENSOR (l)", 18:"RESIDUAL CONNECTION / CHAR TENSOR (r)", 20:"CHAR TENSOR (t)"}

paths = [p for p in fp.solve() if fp.CIRCLE in set(p)]
assert len(paths) == 2
idx = [{c:i for i,c in enumerate(p)} for p in paths]
labels = ["path circling %d" % d[fp.CIRCLE] for d in idx]

facts = {}   # name -> (value_for_path0, value_for_path1)
def add(name, f):
    facts[name] = tuple(f(p, d) for p, d in zip(paths, idx))

# --- global shape ---
add("total cells on the path",            lambda p,d: len(p))
add("highest number (cells minus START/END)", lambda p,d: len(p)-2)
add("number of turns",                    lambda p,d: sum(
        1 for i in range(1, len(p)-1)
        if (p[i][0]-p[i-1][0], p[i][1]-p[i-1][1]) != (p[i+1][0]-p[i][0], p[i+1][1]-p[i][1])))
add("number of straight runs",             lambda p,d: 1 + sum(
        1 for i in range(1, len(p)-1)
        if (p[i][0]-p[i-1][0], p[i][1]-p[i-1][1]) != (p[i+1][0]-p[i][0], p[i+1][1]-p[i][1])))
add("cells NOT on the path",               lambda p,d: N*N - len(p))
add("sum of all path numbers",             lambda p,d: sum(range(1, len(p)-1)))

# --- line counts ---
for r in range(1, N+1):
    add("row %d count" % r, lambda p,d,r=r: sum(1 for (rr,cc) in p if rr == r))
for c in range(1, N+1):
    add("col %d count" % c, lambda p,d,c=c: sum(1 for (rr,cc) in p if cc == c))

# --- counts inside the printed overlay rectangles on the sheet ---
add("cells inside the dark 5x5 block rows3-7 cols3-7",
    lambda p,d: sum(1 for (r,c) in p if 3 <= r <= 7 and 3 <= c <= 7))
add("cells in the left half (cols 1-4)",  lambda p,d: sum(1 for (r,c) in p if c <= 4))
add("cells in the top half (rows 1-4)",   lambda p,d: sum(1 for (r,c) in p if r <= 4))

# --- the number sitting at each cell ---
for r in range(1, N+1):
    for c in range(1, N+1):
        add("number at r%dc%d" % (r,c), lambda p,d,r=r,c=c: d.get((r,c)))

diff = {k:v for k,v in facts.items() if v[0] != v[1]}
same = len(facts) - len(diff)
print("candidate facts tested : %d" % len(facts))
print("facts that differ      : %d   (identical on both paths: %d)" % (len(diff), same))
print()
print("Of the differing facts, which take a value the chain can supply?")
print("(the chain can hand FORWARD PASS one of %s)" % sorted(CHAIN))
print()
hits = []
for k, (a, b) in sorted(diff.items()):
    for v, who in ((a,0), (b,1)):
        if v in CHAIN:
            other = b if who == 0 else a
            if other not in CHAIN:
                hits.append((k, v, labels[who]))
if not hits:
    print("  NONE. No differing fact of this family equals any available chain value")
    print("  while being unambiguous, so the import is not a fact of this kind.")
else:
    for k, v, who in hits:
        print("  %-46s = %-3s selects %s   [%s]" % (k, v, who, CHAIN[v]))
print()
print("The 20 vs 22 split, spelled out:")
for k, (a, b) in sorted(diff.items()):
    if k.startswith("number at"): continue
    print("  %-46s  %-6s vs %-6s" % (k, a, b))
