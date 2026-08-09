"""Re-run the decode search with the CORRECTED fifth parameter (22, not 20)."""
from itertools import permutations, combinations
PH = "Voyages Nearing Zero Descend"; L = PH.replace(" ", "")
DICT = set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())
P = [5, 18, 7, 8, 22, 9]          # region order, corrected
EXP = [5, 18, 7, 8, 22]           # the five that EXPORT (red 9 does not)

def ana(s):
    k="".join(sorted(s.lower())); return sorted(w for w in DICT if len(w)==len(s) and "".join(sorted(w))==k)

print("corrected parameters :", P)
print("A=1..Z=26            :", "".join(chr(64+n) for n in P), " anagrams:", ana("".join(chr(64+n) for n in P)) or "none")
print("exporters only       :", "".join(chr(64+n) for n in EXP), " anagrams:", ana("".join(chr(64+n) for n in EXP)) or "none")
print()
def idx(seq, src, off=1):
    try: return "".join(src[p-off] for p in seq)
    except IndexError: return None
schemes = {
 "phrase 1-based        ": (L, 1), "phrase 0-based        ": (L, 0),
 "phrase w/ spaces      ": (PH, 1), "phrase reversed       ": (L[::-1], 1),
}
for name,(src,off) in schemes.items():
    for lab, seq in (("all six", P), ("exporters", EXP), ("six sorted", sorted(P)),
                     ("six desc", sorted(P, reverse=True)), ("exp sorted", sorted(EXP))):
        s = idx(seq, src, off)
        if not s: continue
        a = ana(s)
        mark = "  <-- WORD" if s.lower() in DICT else ("  ~ anagram: %s" % ",".join(a[:4]) if a else "")
        print("  %s %-11s %-8s%s" % (name, lab, s, mark))
print()
print("5-letter subsets of the six parameter letters that are words:")
six = "".join(chr(64+n) for n in P)
seen=set()
for c in combinations(six,5):
    for w in ana("".join(c)):
        if w not in seen: seen.add(w); print("   ", w.upper())
if not seen: print("    none")
