"""Anchor on the two circled values I am certain of -- region 1 = 5 (GRADIENT FLOW has a
unique solution) and region 6 = 9 -- and find every dictionary word the kiosk phrase can
spell by letter-indexing, consistent with those anchors."""
PHRASE = "Voyages Nearing Zero Descend"
L = PHRASE.replace(" ", "")
DICT = set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())

def positions_for(word, seq):
    """all index tuples (1-based into seq) spelling `word`"""
    res = [()]
    for ch in word:
        nxt = []
        for pref in res:
            for i, c in enumerate(seq, 1):
                if c.lower() == ch: nxt.append(pref + (i,))
        res = nxt
        if not res: return []
    return res

CT_OPTS, FP_OPTS = (8, 12, 18, 20), (20, 22)
print("phrase letters (1-based):")
print("  " + "  ".join("%d=%s" % (i, c) for i, c in enumerate(L, 1)))
print()

for name, seq in (("letters only (25)", L), ("with spaces (28)", PHRASE),
                  ("letters reversed", L[::-1])):
    print("=== indexing %s ===" % name)
    found = []
    for w in DICT:
        if not (3 <= len(w) <= 8): continue
        for t in positions_for(w, seq):
            if t[0] != 5: continue                       # region 1 = 5
            if len(t) == 6 and t[-1] != 9: continue      # region 6 = 9
            if len(t) == 6 and (t[3] not in CT_OPTS or t[4] not in FP_OPTS): continue
            found.append((len(w), w, t))
    six = sorted(set(f for f in found if f[0] == 6))
    print("  6-letter words with tuple (5, ?, ?, CT, FP, 9):", len(six))
    for n, w, t in six: print("     %-10s %s" % (w.upper(), t))
    other = sorted(set(f for f in found if f[0] != 6))
    if other:
        print("  other lengths starting at position 5 (first letter only anchored):", len(other))
        for n, w, t in other[:25]: print("     %-10s %s" % (w.upper(), t))
    print()

print("=== if the exported chain 5,18,7,CT,FP is used and 9 is NOT a letter ===")
for ct in CT_OPTS:
    for fpv in FP_OPTS:
        s = "".join(L[i-1] for i in (5, 18, 7, ct, fpv)).lower()
        tag = "  <-- WORD" if s in DICT else ""
        print("   CT=%2d FP=%2d -> %s%s" % (ct, fpv, s, tag))
        s2 = "".join(L[i-1] for i in (5, 18, ct, 7, fpv)).lower()
        if s2 in DICT: print("        (pencil order) -> %s  <-- WORD" % s2)
