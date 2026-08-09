"""CONFIRMED MECHANISM (from a Jane Street rep): the punch-strip holes, read along the
strip, index the kiosk sentence and spell the password.

Holes are read in strip order, so the password must be a SUBSEQUENCE of the phrase:
its letters appear in increasing position. Enumerate every dictionary word that is."""
PH = "Voyages Nearing Zero Descend"
L  = PH.replace(" ", "").lower()
DICT = [w.strip().lower() for w in open("/tmp/words.txt") if w.strip()]

def positions(word, s):
    """greedy leftmost embedding; returns 1-based positions or None"""
    pos, i = [], 0
    for ch in word:
        j = s.find(ch, i)
        if j < 0: return None
        pos.append(j+1); i = j+1
    return pos

hits = []
for w in DICT:
    if len(w) < 4: continue
    p = positions(w, L)
    if p: hits.append((len(w), w, p))
hits.sort(key=lambda t: (-t[0], t[1]))
print("phrase: %s  (%d letters)" % (L, len(L)))
print("dictionary words that are subsequences of it: %d\n" % len(hits))
print("longest 40:")
for n, w, p in hits[:40]:
    print("  %-12s %s" % (w.upper(), p))
print()
THEME = ["gradient","descend","descent","converge","neuron","tensor","vector","design",
         "engine","assign","reason","season","encode","decoder","여","origin","nascent",
         "ascend","yearn","sonar","grace","genesis","serene","resonance","cadence",
         "voyage","sending","reading","gearing","yearning","earnings","nearing","zeroes"]
print("thematic / notable words among them:")
seen=set()
for n,w,p in hits:
    if w in THEME or (n>=6 and w in ("nearing","earning","gearing","yearns","garden","engine","genesis")):
        if w in seen: continue
        seen.add(w); print("  %-12s %s" % (w.upper(), p))
