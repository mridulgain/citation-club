# size vs strength
import sys
import pickle
from collections import Counter

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

pccs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))
freq = Counter(len(x[0]) for x in pccs)
strength = {}
for x in pccs:
    strength[len(x[0])] = strength.setdefault(len(x[0]), 0) + x[2]
# avg
for x in strength:
    strength[x] /= freq[x]
# output
for i in strength:
    print(i, strength[i])