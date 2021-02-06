# member distribution in pccs
import sys
import pickle
from collections import Counter

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 club_freq_distrib.py [jmlr|prl]")
    exit(0)

pccs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))

freq = Counter(len(x[0]) for x in pccs)
for i in freq:
    print(i, freq[i])
