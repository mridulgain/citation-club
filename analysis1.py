#!/usr/bin/python3
from clubAnalyser import Analysis
club = [2064393185, 2120199875, 2078454212, 2150454853, 2309141562, 76530380, 1969841055, 2195679122, 2146387448, 1954235802, 2258767774, 2165532159]
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
########################################################
'''import networkx as nx
G = nx.Graph()
for i in range(len(club)):
    for j in range(len(club)):
        if len(coauth[i][j]) > 1:
            G.add_edge(i,j)
import matplotlib.pyplot as plt
nx.draw( G )
plt.show()'''
