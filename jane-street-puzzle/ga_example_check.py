"""Verify the rule set against the GRADIENT ACCUMULATION printed EXAMPLE."""
EX = [[5,1,3,4,7,2,6],
      [7,6,2,1,3,4,5],
      [1,5,3,4,6,2,7]]
SUMS = [13,12,8,9,16,8,18]
R, C = len(EX), len(EX[0])
print("rows are permutations of 1..%d:" % C,
      all(sorted(r) == list(range(1, C+1)) for r in EX))
print("column sums match:", [sum(EX[i][c] for i in range(R)) for c in range(C)], "vs", SUMS)
bad = []
for r in range(R):
    for c in range(C):
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==0 and dc==0: continue
                rr,cc = r+dr, c+dc
                if 0<=rr<R and 0<=cc<C and EX[rr][cc]==EX[r][c]:
                    bad.append(((r+1,c+1),(rr+1,cc+1),EX[r][c]))
print("king-move (no equal value among the 8 neighbours) violations:", bad)
