# count number of communities detected in both network
import sys
import pickle

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

coauth = pickle.load(open("results/experiment1/"+journal+".communities_co.bin", 'rb'))
print("co auth community size, modularity", len(coauth), coauth.q)
cit = pickle.load(open("results/experiment1/"+journal+".communities_cit.bin", 'rb'))
print("cit community size", len(cit))
pccs = pickle.load(open("results/experiment1/"+journal+".pccs.bin", 'rb'))
print("pccs", len(pccs))
