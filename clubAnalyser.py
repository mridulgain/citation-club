#!/usr/bin/python3
import rawDataParser as rdp

club = [2064393185, 2120199875, 2078454212, 2150454853, 2309141562, 76530380, 1969841055, 2195679122, 2146387448, 1954235802, 2258767774, 2165532159]
#club = [1977649925, 2468960519, 1972291593, 1572478601, 2048266507, 2171367185, 2038901907, 2042048789, 2158987803, 168172700, 1980701853, 2086114595, 2099091510, 2279633593, 2150887997, 2609987651, 2093953614, 60139091, 2330451, 2113868374, 2122791383, 297432538, 670306551, 2148448995, 2122328552, 289005672, 167589996, 2285762679, 2584127737, 251023228, 2107302653, 2296948990]
print(club)
papers, authors = rdp.load_data('./data/prl/prl_dblp.json')
#papers, authors = rdp.load_data('./data/jmlr/jmlr_dblp.json')

# co authorship matrix formation
coauth = rdp.get_collab(club, './data/prl/prl_dblp.json')
# output
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

# reference count
ref = [[set() for x in range(len(club))] for y in range(len(club))]
for i in range(len(club)):
    i_papers = authors[club[i]]['papers']
    for k in i_papers:
        i_paper_ref = papers[k]['references']
        for j in range(len(club)):
            j_papers = authors[club[j]]['papers']
            tmp = set()
            for l in set(j_papers).intersection(i_paper_ref):
                # i cites j with k->l, author(k)=i, author(l)=j
                tmp.add((k, l))
            ref[i][j].update(tmp)
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
# total citation from journal = sum(len(cited_by) for all his papers)
n_cit = [0] * len(club)
for i in range(len(club)):
    i_papers = authors[club[i]]['papers']
    for p in i_papers:
        n_cit[i] += len(papers[p]['cited_by'])
print("Total citation from journal:---------------------------------")
for x in zip(club, n_cit):
    print(x)
# totatl citation from club = len( row wise union of ref matrix )
n_cit_club = [None] * len(club)
for i in range(len(club)):
    tmp = set()
    for j in range(len(club)):
        tmp.update(ref[j][i])
    n_cit_club[i] = tmp
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
