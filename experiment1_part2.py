# calculate and store pcc details for all pccs for a given journal
from clubAnalyser import Analysis
import sys
import pickle

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 experiment3.py [jmlr|prl]")
    exit(0)

db = "./data/" + journal + "/" + journal + "_dblp.json"

pccs = pickle.load(open('./results/experiment1/' + journal + '.pccs.bin', 'rb'))
score = []
pcc_scc_score = []
for c in pccs:
    ca = Analysis(list(c), db)
    sccs = ca.get_scc()
    total_strength = 0
    scc_list = []
    for i in sccs:
        total_strength += i.weight
        
    print(len(c), total_strength)
    score.append(total_strength)
    pcc_scc_score.append([c, sccs, total_strength])
#print("max strength", max(score))
#pickle.dump(score, open("./results/experiment1/" + journal + ".score.bin", 'wb'))
pickle.dump(pcc_scc_score, open("./results/experiment1/" + journal + ".pcc_details.bin", 'wb'))
