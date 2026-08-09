"""Each card carries one printed circle on its punch strip, at a card-specific position.
Reported positions: 1, 2, 4, 8, 12 (five of the six; the red one is GRADIENT ACCUMULATION).
Treat the circle position as an index into the kiosk phrase and hunt for real words."""
from itertools import permutations
PH = "Voyages Nearing Zero Descend"
L  = PH.replace(" ", "")
DICT = set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())
KNOWN = [1, 2, 4, 8, 12]
REG = ["GradFlow", "Residual", "DualParam", "CharTensor", "FwdPass", "GradAccum"]

def look(seq, src, off=1):
    try: return "".join(src[p-off] for p in seq)
    except IndexError: return None

print("phrase letters:", " ".join("%d=%s" % (i, c) for i, c in enumerate(L, 1)))
print()
hits = []
# six positions = the five known + one unknown X, assigned to the six regions in some order
for X in range(1, 26):
    pool = KNOWN + [X]
    for perm in set(permutations(pool)):
        for name, src, off in (("phrase letters", L, 1), ("phrase 0-based", L, 0),
                               ("with spaces", PH, 1), ("letters reversed", L[::-1], 1)):
            w = look(perm, src, off)
            if w and w.lower() in DICT:
                hits.append((w.lower(), X, perm, name))
# also: only the five known positions form the word (final circle excluded)
for perm in set(permutations(KNOWN)):
    for name, src, off in (("phrase letters", L, 1), ("phrase 0-based", L, 0),
                           ("with spaces", PH, 1), ("letters reversed", L[::-1], 1)):
        w = look(perm, src, off)
        if w and w.lower() in DICT:
            hits.append((w.lower(), None, perm, name + " [5 only]"))

seen = set()
print("=== real words ===")
for w, X, perm, name in sorted(hits):
    k = (w, name)
    if k in seen: continue
    seen.add(k)
    order = " ".join("%s@%d" % (REG[i], p) for i, p in enumerate(perm))
    print("  %-9s  [%s]%s" % (w.upper(), name, ("  6th pos = %d" % X) if X else ""))
    print("       %s" % order)
if not hits: print("  none")
