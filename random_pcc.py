# choose 10 random pcc and their strength
import sys
import pickle
import random
try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 experiment3.py [jmlr|prl]")
    exit(0)
pccs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))
if journal == "prl":
    journal = "cj"
else:
    journal = "oj"
sample = [x for x in range(len(pccs))]
sample_ix = random.sample(sample, 10) # select 10 indices randomly
avg_strength = 0
avg_size = 0
for i in sample_ix:
    print(journal+".pcc["+str(i+1)+"]", "&", len(pccs[i][0]), "&", round(pccs[i][2], 4), r"\\")
    avg_strength += round(pccs[i][2], 4)
    avg_size += len(pccs[i][0])
print("\hfill\nAverage size ", round(avg_size/10, 4))
print("\hfill\nAverage strength ", round(avg_strength/10, 4))
