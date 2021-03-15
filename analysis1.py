#!/usr/bin/python3
from clubAnalyser import Analysis
club = [2632670945, 2550077121, 216075398, 2092308615, 200915819, 2148166381, 113165838, 2481588367, 2079098163, 2189485621, 2192965622, 127393751, 2050734970, 254993851, 2973729724]
fin = './data/prl/prl_dblp.json'
# club = [2712128676, 2029196934, 2076429416, 2107833897, 2167354121, 2164775409, 1794038515, 2117210965, 971226294, 2060257498, 2151570909, 2102688157]
# fin = './data/jmlr/jmlr_dblp.json'
print(club)
ca = Analysis(club, fin)
############################################################# collab
coauth = ca.get_coauth_matrix()
print("Coauthorship count-------------------------------------------")
for i in range(len(club)):
    print("auth[",i+1,"]", end = "&")
    for j in range(len(club)):
        print(len(coauth[i][j]), end="&")
    print("\\ \hline")
print("Coauthorship details-----------------------------------------")
for i in range(len(club)):
    for j in range(len(club)):
        print(coauth[i][j], end=" | ")
    print("\n")

###################################################### projection
ref = ca.get_reference_matrix()
# output
print("Citation details :---------------------------------------- ")
for i in range(len(club)):
    for j in range(len(club)):
        print(ref[i][j], end=" | ")
    print("\n")
print("Citation count :---------------------------------------- ")
for i in range(len(club)):
    print("auth["+str(i+1)+"]", end = " & ")
print("\\ \hline")
for i in range(len(club)):
    print("auth["+str(i+1)+"]", end = " & ")
    for j in range(len(club)):
        print(len(ref[i][j]), end=" & ")
    print("\\ \hline")
###################################################### self, club & journal cit
n_journal_cit = ca.count_journal_cit()
club_cit = ca.get_club_cit()
self_cit = ca.get_self_cit()
print("self citation, club citation, journal citation:---------------------------------")
for i, x, y , z in zip(club, self_cit, club_cit, n_journal_cit):
    print(i, "&", len(x), "&", len(y), "&", z, "&", r"\\")
######################################################## club strength
sccs = ca.get_scc()
total_strength = 0
for i in sccs:
    #print(i.members, i.weight)
    total_strength += i.weight
print("club score/strength ", total_strength)
'''import networkx as nx
G = nx.Graph()
for i in range(len(club)):
    for j in range(len(club)):
        if len(coauth[i][j]) > 1:
            G.add_edge(i,j)
import matplotlib.pyplot as plt
nx.draw( G )
plt.show()'''
