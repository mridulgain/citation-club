#!/usr/bin/python3

# input: author id of any one member of the pcc 
# output: visualisation of the whole pcc (with masked auth_id)
#           for both projection & coauthorship matrix
import sys
import pickle
from clubAnalyser import Analysis
from mask_author_id import search_author

try:
    journal = sys.argv[1]
    author = int(sys.argv[2])
except IndexError:
    #journal = "prl"
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

pccs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))
fin = './data/' + journal + '/' + journal + '_dblp.json'
pcc_index = search_author(pccs, author)
if pcc_index == -1:
    print("pcc not found in given journal")
    exit(0)
print("pcc: ", pcc_index+1)
club = list(pccs[pcc_index][0])

ca = Analysis(club, fin)
#####################################graph drawing###############################################
ca.masked_visualise("results/"+journal+".pcc"+str(pcc_index+1), engine='circo')


