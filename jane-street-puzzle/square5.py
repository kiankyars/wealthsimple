"""The kiosk phrase is exactly 25 letters and three of the six grids are 5x5. Write the
phrase into a 5x5 square and try every plausible reading order and indexing."""
L = "VoyagesNearingZeroDescend"
DICT = set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())
P = [5, 18, 7, 8, 20, 9]                 # the six parameters, region order
STRIP = [1, 2, 4, 8, 12]                 # strip circles, regions 2..6

g = [list(L[r*5:(r+1)*5]) for r in range(5)]
print("phrase as a 5x5 square:")
for r in g: print("   ", " ".join(r))
print()

def rowwise():   return [g[r][c] for r in range(5) for c in range(5)]
def colwise():   return [g[r][c] for c in range(5) for r in range(5)]
def boustro():   return [g[r][c] for r in range(5) for c in (range(5) if r%2==0 else range(4,-1,-1))]
def boustroC():  return [g[r][c] for c in range(5) for r in (range(5) if c%2==0 else range(4,-1,-1))]
def diagwise():
    out=[]
    for s in range(9):
        for r in range(5):
            c=s-r
            if 0<=c<5: out.append(g[r][c])
    return out
def spiral():
    m=[row[:] for row in g]; out=[]
    while m:
        out+= m.pop(0)
        m=[list(x) for x in zip(*m)][::-1]
    return out
ORDERS = {"rowwise":rowwise(), "columnwise":colwise(), "boustrophedon rows":boustro(),
          "boustrophedon cols":boustroC(), "diagonals":diagwise(), "spiral":spiral()}

def show(name, seq, idx, label):
    s = "".join(seq[i-1] for i in idx if 1 <= i <= 25)
    flag = "   <-- WORD" if s.lower() in DICT else ""
    print("  %-20s %-14s %s%s" % (name, label, s, flag))
    return s.lower()

hits=[]
for name, seq in ORDERS.items():
    for label, idx in (("params", P), ("params rev", P[::-1]), ("params asc", sorted(P)),
                       ("params desc", sorted(P, reverse=True)), ("strip", STRIP),
                       ("strip+params", STRIP)):
        if label == "strip+params": continue
        s = show(name, seq, idx, label)
        if s in DICT: hits.append((name, label, s))
print()
# coordinates: read each parameter as (row, col) in the 5x5 via the grids' circled cells
CIRC = {"GRADIENT FLOW":(3,4), "DUAL PARAMETER SPACE":(4,1), "CHAR TENSOR":(2,4)}
print("letters at the 5x5 grids' own circled cell positions:")
for k,(r,c) in CIRC.items(): print("   %-24s r%dc%d -> %s" % (k, r, c, g[r-1][c-1]))
print()
print("words found:", hits or "none")
