import sys
import pickle
try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 experiment3.py [jmlr|prl]")
    exit(0)
clubs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))
clubs = sorted(clubs, key = lambda x : len(x[0]))
for c in clubs:
    print("pcc: ", c[0], " size: ", len(c[0]))
    print("SCC:")
    for s in c[1]:
        print(s.members, s.weight)
    print("total score:", c[2])
    print("")
