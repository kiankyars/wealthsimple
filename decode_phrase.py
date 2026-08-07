"""The kiosk at parameterspace.wondermakr.com/en/answer says:

    "Use this phrase to arrive at your final answer:  Voyages Nearing Zero Descend"

and takes a TEXT answer (letters/digits/punctuation, max 25 chars). So the six circled
numbers must decode against that phrase. Try every plausible scheme and keep only results
that are real words (or anagrams of real words)."""
from itertools import permutations

PHRASE = "Voyages Nearing Zero Descend"
LETTERS = PHRASE.replace(" ", "")                     # 25 letters
WORDS = PHRASE.split()
print("phrase:", PHRASE)
print("letters (no spaces): %s  -> %d letters" % (LETTERS, len(LETTERS)))
print("word lengths:", [len(w) for w in WORDS], "= %d" % sum(len(w) for w in WORDS))
print("with spaces: %d chars" % len(PHRASE))
print()

DICT = set(w.strip().lower() for w in open("/tmp/words.txt") if w.strip())
def is_word(s):  return s.lower() in DICT
def anagrams(s):
    k = "".join(sorted(s.lower()))
    return [w for w in DICT if len(w) == len(s) and "".join(sorted(w)) == k]

# the confirmed chain, plus the two places with residual freedom
CHAINS = []
for ct in (8, 12, 18, 20):
    for fpv in (20, 22):
        CHAINS.append(("GF5 RC18 DP7 CT%d FP%d GA9" % (ct, fpv), [5, 18, 7, ct, fpv, 9]))
# also the alternative order the pencil notes assumed (CT before DP)
for ct in (8, 12, 18, 20):
    for fpv in (20, 22):
        CHAINS.append(("GF5 RC18 CT%d DP7 FP%d GA9  (pencil order)" % (ct, fpv), [5, 18, ct, 7, fpv, 9]))

def schemes(nums):
    out = {}
    orders = {"region order": nums, "reversed": nums[::-1],
              "ascending": sorted(nums), "descending": sorted(nums, reverse=True)}
    for oname, seq in orders.items():
        # A=1..Z=26
        if all(1 <= n <= 26 for n in seq):
            out["A1Z26, %s" % oname] = "".join(chr(64+n) for n in seq)
        # index the phrase letters (1-based and 0-based)
        if all(1 <= n <= len(LETTERS) for n in seq):
            out["phrase letters 1-based, %s" % oname] = "".join(LETTERS[n-1] for n in seq)
        if all(0 <= n < len(LETTERS) for n in seq):
            out["phrase letters 0-based, %s" % oname] = "".join(LETTERS[n] for n in seq)
        # index the phrase including spaces
        if all(1 <= n <= len(PHRASE) for n in seq):
            out["phrase w/ spaces 1-based, %s" % oname] = "".join(PHRASE[n-1] for n in seq)
        # drop the final (non-exporting) number
        s2 = seq[:-1] if oname == "region order" else None
        if s2 and all(1 <= n <= len(LETTERS) for n in s2):
            out["phrase letters, first five only"] = "".join(LETTERS[n-1] for n in s2)
    return out

hits = []
allres = {}
for label, nums in CHAINS:
    for sname, s in schemes(nums).items():
        allres.setdefault((sname, s), []).append(label)
        if is_word(s):
            hits.append(("EXACT WORD", sname, s, label))
        else:
            for a in anagrams(s):
                hits.append(("anagram -> %s" % a.upper(), sname, s, label))

print("=== results that are real words or anagram to one ===")
if not hits:
    print("  none")
seen = set()
for kind, sname, s, label in sorted(hits):
    if (kind, s) in seen: continue
    seen.add((kind, s))
    print("  %-26s %-40s %-8s  [%s]" % (kind, sname, s, label))
print()
print("=== what each scheme yields for the confirmed chain 5,18,7,8,20,9 ===")
for sname, s in sorted(schemes([5,18,7,8,20,9]).items()):
    print("  %-42s %s" % (sname, s))
