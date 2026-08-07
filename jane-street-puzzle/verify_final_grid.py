"""Independent re-check of the REGION 6 answer grid (no solver code reused)."""
G = [[5,3,1,7,8,6,9,4,2],
     [8,6,9,5,2,4,3,7,1],
     [1,4,7,3,9,8,5,2,6],
     [9,2,5,4,6,1,3,8,7]]
PRINTED_CELLS = {(1,3):1,(1,6):6,(1,8):4,(1,9):2,(2,1):8,(2,2):6,(3,6):8,
                 (4,1):9,(4,3):5,(4,5):6,(4,9):7}
PRINTED_SUMS = {1:23,2:15,4:19,5:25,6:19,8:21,9:16}
R, C = 4, 9
print("rows are permutations of 1..9 :", all(sorted(r)==list(range(1,10)) for r in G))
sums = [sum(G[i][c] for i in range(R)) for c in range(C)]
print("column sums                   :", sums)
print("match all printed sums        :", all(sums[c-1]==v for c,v in PRINTED_SUMS.items()))
print("blank sums are c3 =", sums[2], "and c7 =", sums[6])
print("match all printed cell givens :", all(G[r-1][c-1]==v for (r,c),v in PRINTED_CELLS.items()))
viol=[]
for r in range(R):
    for c in range(C):
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==0 and dc==0: continue
                rr,cc=r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]==G[r][c]: viol.append(((r+1,c+1),(rr+1,cc+1)))
print("king-move violations          :", len(viol)//2)
print("total of all cells            :", sum(sum(r) for r in G), "(must be 4x45 = 180)")
print()
print("RED-CIRCLED CELL r1c7         :", G[0][6], " <-- FINAL ANSWER")
