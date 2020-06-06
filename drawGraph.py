#!/usr/bin/python3
import rawDataParser as rdp

club = [2064393185, 2120199875, 2078454212, 2150454853, 2309141562, 76530380, 1969841055, 2195679122, 2146387448, 1954235802, 2258767774, 2165532159]
#club = [1977649925, 2468960519, 1972291593, 1572478601, 2048266507, 2171367185, 2038901907, 2042048789, 2158987803, 168172700, 1980701853, 2086114595, 2099091510, 2279633593, 2150887997, 2609987651, 2093953614, 60139091, 2330451, 2113868374, 2122791383, 297432538, 670306551, 2148448995, 2122328552, 289005672, 167589996, 2285762679, 2584127737, 251023228, 2107302653, 2296948990]
print(club)
papers, authors = rdp.load_data('./data/prl/prl_dblp.json')
# papers, authors = rdp.load_data('./data/jmlr/jmlr_dblp.json')

# co authorship matrix formation
coauth = [[set() for x in range(len(club))] for y in range(len(club))]
for i in range(len(club)):
    for j in range(i, len(club)):
        paper_i = authors[club[i]]['papers']
        paper_j = authors[club[j]]['papers']
        coauth[j][i] = coauth[i][j] = set(paper_i).intersection(paper_j)
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
#####################################graph drawing#############################################'''
from graphviz import Digraph
g = Digraph(comment = "induced sub graph", engine='dot')  # engine= dot(default), neato, fdp
for i in club:
    g.node(str(i))
with g.subgraph(name='coauth') as c:
    c.attr('edge', dir='none', color='red')
    for i in range(len(club)):
        for j in range(i, len(club)):
            if i!=j and len(coauth[i][j]) > 0:
                c.edge(str(club[i]), str(club[j]), label=str(len(coauth[i][j])))
with g.subgraph(name='cit') as c:
    for i in range(len(club)):
        for j in range(len(club)):
            if len(ref[i][j]) > 0:
                g.edge(str(club[i]), str(club[j]), label=str(len(ref[i][j])))
#print(g.source)
g.render("results/induced_subg.gv", view=True)
#g.view()
##########################strongly connected components for induced subg#########################
'''import networkx as nx
g = nx.DiGraph()
for i in range(len(club)):
    for j in range(len(club)):
        if len(ref[i][j]) > 0:
            g.add_edge(club[i], club[j])
cc = nx.strongly_connected_components(g)
for i in cc:
    print(i)
import matplotlib.pyplot as plt
nx.draw_kamada_kawai(g)
plt.show()'''
