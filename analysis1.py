#!/usr/bin/python3
from clubAnalyser import Analysis
club = [2530972163, 2163470342, 2953368070, 2916255243, 2786860172, 2493535503, 1999536656, 2806021778, 2719544221, 2191573790, 2118003487, 2785462173, 2435795745, 2762446754, 2131084071, 2106866729, 2163830057, 2299437103, 2153170226, 2617328699, 2307711420, 2639933372, 2181331778, 2111317318, 2486321479, 2275853904, 2525533649, 2618462548, 2054682710, 2131585752, 2110542169, 2128616155, 2308378844, 2648045154, 2419996774, 2639260782, 2776399727, 2079150322, 2141729011, 2717155834, 2593217274, 2980864762, 2306900094, 2107803903]
# club = [1977649925, 2468960519, 1972291593, 1572478601, 2048266507, 2171367185, 2038901907, 2042048789, 2158987803, 168172700, 1980701853, 2086114595, 2099091510, 2279633593, 2150887997, 2609987651, 2093953614, 60139091, 2330451, 2113868374, 2122791383, 297432538, 670306551, 2148448995, 2122328552, 289005672, 167589996, 2285762679, 2584127737, 251023228, 2107302653, 2296948990]
fin = './data/prl/prl_dblp.json'
# fin = './data/jmlr/jmlr_dblp.json'
print(club)
ca = Analysis(club, fin)
############################################################# collab
coauth = ca.get_coauth_matrix()
print("Coauthorship count-------------------------------------------")
for i in range(len(club)):
    for j in range(len(club)):
        print(len(coauth[i][j]), end=" | ")
    print("\n")
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
    for j in range(len(club)):
        print(len(ref[i][j]), end=" | ")
    print("\n")
###################################################### journal cit
n_cit = ca.count_journal_cit()
print("Total citation from journal:---------------------------------")
for x in zip(club, n_cit):
    print(x)
###################################################### club cit
n_cit_club = ca.get_club_cit()
print("Totalo citation from club:-----------------------------------")
for ix, x in enumerate(club):
    print(x, len(n_cit_club[ix]))
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
