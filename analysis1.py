#!/usr/bin/python3
from clubAnalyser import Analysis
club = [2530972163, 2953368070, 2163470342, 2916255243, 2646329355, 1999536656, 2106866729, 2299437103, 2150813751, 2119564347, 2617328699, 2275853904, 2054682710, 2648045154, 2419996774, 2608506984, 2639260782, 2184381038, 2936217711, 2689882230, 2907377662, 2312077945, 2306900094, 2136632959, 2428571269, 2633795720, 2223163528, 2786860172, 2806021778, 2958999215, 2289308872, 2651163857, 2131585752, 2128616155, 2308378844, 2098147036, 2621082335, 2515562216, 2990873832, 2079150322, 2141729011, 2593217274, 2980864762, 2194702591, 2107803903, 2131974911, 2171932422, 2658314510, 2493535503, 2959698198, 2766192925, 2191573790, 2118003487, 2435795745, 2131084071, 2163830057, 2153170226, 2897493812, 2659730751, 2181331778, 2111317318, 2486321479, 2664185679, 2974289232, 2618462548, 2110542169, 2521906021, 2788252523, 2776399727, 2256830846, 2568784767, 2644755847, 2488838541, 2775994258, 2719544221, 2785462173, 2762446754, 2307711420, 2639933372, 2788907974, 2957313488, 2525533649, 2663206871, 2717155834, 2432833534]
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
    print(i, "&", len(x), "&", len(y), "&", z, r"\\")
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
