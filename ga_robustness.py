"""Exhaustive robustness analysis of REGION 6 (GRADIENT ACCUMULATION).

Answers, with no reliance on the earlier solver's algorithm:
  1. how many grids satisfy ALL the printed data (re-derived row-wise, a different method)
  2. is the pencil grid on the sheet among them
  3. which single extra fact makes it unique, and what r1c7 becomes
  4. can ANY single extra fact -- column total or cell -- ever force r1c7 = 8
"""
from itertools import permutations
import grad_accum as ga

USER = [[5,3,1,7,8,6,9,4,2],
        [8,6,9,4,2,1,7,3,5],
        [1,4,3,7,9,8,5,6,2],
        [9,2,5,1,6,4,3,8,7]]
key = lambda g: tuple(tuple(r) for r in g)

def king_ok(g):
    for r in range(4):
        for c in range(9):
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr==0 and dc==0: continue
                    rr,cc=r+dr,c+dc
                    if 0<=rr<4 and 0<=cc<9 and g[rr][cc]==g[r][c]: return False
    return True

def independent_solve():
    """Different algorithm: enumerate rows 1 and 4, then solve rows 2/3 column-pairwise."""
    G, S = ga.GIVEN, ga.SUMS
    def rowopts(r):
        fx={c:v for (rr,c),v in G.items() if rr==r}
        return [p for p in permutations(range(1,10)) if all(p[c-1]==v for c,v in fx.items())]
    r1s, r4s = rowopts(1), rowopts(4)
    f2={c:v for (r,c),v in G.items() if r==2}
    f3={c:v for (r,c),v in G.items() if r==3}
    known=sorted(S); blank=[c for c in range(1,10) if c not in S]
    out=[]
    for r1 in r1s:
        for r4 in r4s:
            tg=[]; ok=True
            for c in known:
                t=S[c]-r1[c-1]-r4[c-1]
                if not (2<=t<=18): ok=False; break
                tg.append((c,t))
            if not ok: continue
            r2=[0]*9; r3=[0]*9
            def dfs(i,u2,u3):
                if i==len(tg):
                    l2=[d for d in range(1,10) if not u2>>d&1]
                    l3=[d for d in range(1,10) if not u3>>d&1]
                    for p2 in permutations(l2):
                        if any(c in f2 and f2[c]!=p2[j] for j,c in enumerate(blank)): continue
                        for p3 in permutations(l3):
                            if any(c in f3 and f3[c]!=p3[j] for j,c in enumerate(blank)): continue
                            rr2,rr3=r2[:],r3[:]
                            for j,c in enumerate(blank): rr2[c-1]=p2[j]; rr3[c-1]=p3[j]
                            cand=[list(r1),rr2,rr3,list(r4)]
                            if king_ok(cand): out.append(cand)
                    return
                c,t=tg[i]
                for a in range(max(1,t-9), min(9,t-1)+1):
                    b=t-a
                    if u2>>a&1 or u3>>b&1: continue
                    if c in f2 and f2[c]!=a: continue
                    if c in f3 and f3[c]!=b: continue
                    r2[c-1]=a; r3[c-1]=b
                    dfs(i+1,u2|1<<a,u3|1<<b)
                    r2[c-1]=0; r3[c-1]=0
            dfs(0,0,0)
    return out

ind = independent_solve()
col = ga.solve()
print("independent row-wise solver  :", len(ind), "grids")
print("original column-wise solver  :", len(col), "grids")
print("the two agree exactly        :", {key(g) for g in ind} == {key(g) for g in col})
print()
S = sorted({key(g) for g in ind})
grids = [[list(r) for r in g] for g in S]
for i, g in enumerate(grids, 1):
    c3=sum(g[r][2] for r in range(4)); c7=sum(g[r][6] for r in range(4))
    mark = "   <-- the pencil grid on the sheet" if key(g)==key(USER) else ""
    print("grid %d: r1c7 = %d   blank totals col3=%2d col7=%2d%s" % (i, g[0][6], c3, c7, mark))
print()
print("pencil grid satisfies every printed constraint:", key(USER) in {key(g) for g in ind})
print()
print("--- ANY single extra fact, and what it leaves ---")
print("(the printed data already pins the answer down to these 3 grids, so an extra")
print(" fact can only select a subset of them)")
print()
print("a) a blank COLUMN TOTAL")
for c in (3,7):
    vals = sorted({sum(g[r][c-1] for r in range(4)) for g in grids})
    for v in vals:
        keep=[i+1 for i,g in enumerate(grids) if sum(g[r][c-1] for r in range(4))==v]
        ans=sorted({grids[i-1][0][6] for i in keep})
        print("   col%d = %-2d -> grids %s -> r1c7 in %s%s" %
              (c, v, keep, ans, "   UNIQUE" if len(keep)==1 else ""))
print()
print("b) a single CELL value (all 4x9x9 possibilities)")
forces = {}
for r in range(4):
    for c in range(9):
        if (r+1,c+1) in ga.GIVEN: continue
        for v in range(1,10):
            keep=[i+1 for i,g in enumerate(grids) if g[r][c]==v]
            if len(keep)==1:
                forces.setdefault(grids[keep[0]-1][0][6], set()).add(keep[0])
for ans in sorted(forces):
    print("   can force r1c7 = %d  (selecting grid %s)" % (ans, sorted(forces[ans])))
print()
print("c) can r1c7 = 8 ever be forced?  Only by selecting grid",
      [i+1 for i,g in enumerate(grids) if g[0][6]==8])
g8 = [g for g in grids if g[0][6]==8][0]
print("   that grid's blank totals are col3=%d col7=%d -- identical to grid %d's," %
      (sum(g8[r][2] for r in range(4)), sum(g8[r][6] for r in range(4)),
       [i+1 for i,g in enumerate(grids) if g[0][6]==9 and
        sum(g[r][2] for r in range(4))==sum(g8[r][2] for r in range(4))][0]))
print("   so NO column-total import can ever isolate it. A column total of 18 or 24")
print("   leaves r1c7 ambiguous (8 or 9); only 20 or 22 give a unique grid, and both")
print("   give r1c7 = 9.")
