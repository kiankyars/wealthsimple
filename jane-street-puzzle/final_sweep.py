"""Definitive sweep with FORWARD PASS = 22, across every remaining degree of freedom.
CHAR TENSOR's export is still one of {8,12,18,20} (it depends which cell the imported G
lands in), so sweep that too. Report anything that is a real word."""
from itertools import permutations, combinations
PH="Voyages Nearing Zero Descend"; L=PH.replace(" ","")
DICT=set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())
def ana(s):
    k="".join(sorted(s.lower()))
    return sorted(w for w in DICT if len(w)==len(s) and "".join(sorted(w))==k)

SRC = {"letters":(L,1), "letters0":(L,0), "spaces":(PH,1), "reversed":(L[::-1],1)}
found=[]
for CT in (8,12,18,20):
    P=[5,18,7,CT,22,9]; EXP=P[:5]
    A="".join(chr(64+n) for n in P)
    for label, seq in (("all6",P),("exp5",EXP)):
        s="".join(chr(64+n) for n in seq)
        if s.lower() in DICT: found.append(("A1Z26 %s CT=%d"%(label,CT), s, "WORD"))
        for a in ana(s): found.append(("A1Z26 %s CT=%d"%(label,CT), s, "anagram->"+a))
        # 5-letter subsets of the six letters
        if label=="all6":
            for c in combinations(s,5):
                for a in ana("".join(c)): found.append(("A1Z26 sub CT=%d"%CT, "".join(c), "anagram->"+a))
    for sname,(src,off) in SRC.items():
        for label, seq in (("all6",P),("exp5",EXP),("sorted",sorted(P)),("desc",sorted(P,reverse=True)),
                           ("exp sorted",sorted(EXP))):
            try: w="".join(src[p-off] for p in seq)
            except IndexError: continue
            if w.lower() in DICT: found.append(("%s %s CT=%d"%(sname,label,CT), w, "WORD"))
            for a in ana(w): found.append(("%s %s CT=%d"%(sname,label,CT), w, "anagram->"+a))
seen=set(); out=[]
for k in found:
    if k[1:] in seen: continue
    seen.add(k[1:]); out.append(k)
print("real words / anagrams found across the whole sweep:")
for how, raw, what in out: print("   %-26s %-8s %s" % (how, raw, what))
if not out: print("   none")
