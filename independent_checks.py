"""Independent re-derivations, all searching in the OPPOSITE direction from the
original solvers, with different pruning. Agreement = strong confirmation."""
import sys
sys.setrecursionlimit(200000)

# ============ FORWARD PASS, searched backwards from END ============
import forward_pass as fp
N = fp.N
def fp_reverse():
    on=[[False]*(N+2) for _ in range(N+2)]
    rc=[0]*(N+2); cc=[0]*(N+2)
    sols=[]; path=[]
    def full2x2(r,c):
        for dr in(-1,0):
            for dc in(-1,0):
                r0,c0=r+dr,c+dc
                if 1<=r0 and r0+1<=N and 1<=c0 and c0+1<=N:
                    if on[r0][c0] and on[r0][c0+1] and on[r0+1][c0] and on[r0+1][c0+1]: return True
        return False
    def rec(r,c):
        on[r][c]=True; rc[r]+=1; cc[c]+=1; path.append((r,c))
        over = any(rc[k]>v for k,v in fp.ROW_CNT.items()) or any(cc[k]>v for k,v in fp.COL_CNT.items())
        if not over and not full2x2(r,c):
            if (r,c)==fp.START:
                if all(rc[k]==v for k,v in fp.ROW_CNT.items()) and all(cc[k]==v for k,v in fp.COL_CNT.items()):
                    sols.append(list(reversed(path)))
            else:
                for nr,nc in ((r,c+1),(r,c-1),(r+1,c),(r-1,c)):      # different move order
                    if 1<=nr<=N and 1<=nc<=N and not on[nr][nc]: rec(nr,nc)
        path.pop(); cc[c]-=1; rc[r]-=1; on[r][c]=False
    rec(*fp.END)
    return sols

a = {tuple(p) for p in fp.solve()}
b = {tuple(p) for p in fp_reverse()}
print("FORWARD PASS")
print("  forward search : %d paths" % len(a))
print("  reverse search : %d paths" % len(b))
print("  identical sets : %s" % (a == b))
viable = [p for p in sorted(b) if fp.CIRCLE in set(p)]
print("  paths with a number at the printed circle r7c3: %d" % len(viable))
print("  their circled values: %s" % sorted({p.index(fp.CIRCLE) for p in viable}))

# ============ RESIDUAL CONNECTION, searched backwards from FINISH ============
import residual_connection as rc
def rc_reverse(import_cell, import_val):
    grid=[row[:] for row in rc.GRID]
    grid[import_cell[0]][import_cell[1]]=import_val
    target=set(rc.VALUES)|{import_val}
    n=rc.N; seen=[[False]*n for _ in range(n)]; sols=[]
    def go(r,c,have,path):
        if (r,c)==rc.START:
            if have==target: sols.append(list(reversed(path)))
            return
        for nr,nc in ((r,c-1),(r-1,c),(r,c+1),(r+1,c)):
            if not(0<=nr<n and 0<=nc<n) or seen[nr][nc]: continue
            v=grid[nr][nc]
            if v is None or v=="F": continue
            if v=="S":
                seen[nr][nc]=True; path.append((nr,nc)); go(nr,nc,have,path)
                path.pop(); seen[nr][nc]=False; continue
            if v in have: continue
            seen[nr][nc]=True; path.append((nr,nc)); have.add(v)
            go(nr,nc,have,path)
            have.discard(v); path.pop(); seen[nr][nc]=False
    seen[rc.FINISH[0]][rc.FINISH[1]]=True
    go(rc.FINISH[0],rc.FINISH[1],set(),[rc.FINISH])
    return sols, grid
print()
print("RESIDUAL CONNECTION")
tot_f=tot_r=0
for cell in rc.BLANKS:
    for v in range(1,22):
        f,_=rc.solve(cell,v); r_,_g=rc_reverse(cell,v)
        tot_f+=len(f); tot_r+=len(r_)
        if len(f)!=len(r_): print("   MISMATCH at r%dc%d=%d: %d vs %d"%(cell[0]+1,cell[1]+1,v,len(f),len(r_)))
print("  total solutions over all (blank, value) pairs: forward %d, reverse %d, agree %s"
      % (tot_f, tot_r, tot_f==tot_r))
f5,g5 = rc.solve((3,4),5); r5,_ = rc_reverse((3,4),5)
print("  import 5 at r4c5: forward %d path, reverse %d path, same path %s"
      % (len(f5), len(r5), f5[0]==r5[0]))
print("  9th square value: %d" % g5[f5[0][9][0]][f5[0][9][1]])

# ============ GRADIENT FLOW, numbered backwards from 25 ============
import gradient_flow as gf
def gf_reverse():
    cells=gf.CELLS; sols=[]; used=set(); seq={}
    fixed={v:k for k,v in gf.NUM.items()}
    def rec(k):
        if k==0: sols.append(dict(seq)); return
        cands=[fixed[k]] if k in fixed else [c for c in cells if c not in used]
        for c in cands:
            if c in used: continue
            if k<25 and seq.get(k+1) is not None and seq[k+1] not in gf.SUCC[c]: continue
            used.add(c); seq[k]=c
            rec(k-1)
            del seq[k]; used.discard(c)
    rec(25)
    return sols
print()
print("GRADIENT FLOW")
r = gf_reverse()
print("  reverse (25 down to 1) search: %d solution(s)" % len(r))
inv = {v:k for k,v in r[0].items()}
grid=[[0]*5 for _ in range(5)]
for num,cell in r[0].items(): grid[cell[0]-1][cell[1]-1]=num
fwd = gf.solve()[0]
fgrid=[[0]*5 for _ in range(5)]
for cell,num in fwd.items(): fgrid[cell[0]-1][cell[1]-1]=num
print("  matches the forward search: %s" % (grid==fgrid))
print("  circled r3c4 = %d" % grid[2][3])
