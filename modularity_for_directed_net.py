"""
The following error says that modularity calculation for directed graph is not implemented
----
File "/home/mridul/playground/citation-club/env/lib/python3.8/site-packages/igraph/__init__.py", line 898, in modularity
    return GraphBase.modularity(self, membership.membership, weights)
igraph._igraph.InternalError: Error at ../../../source/igraph/src/community.c:921: modularity is implemented for undirected graphs, Invalid value
----
So we convert our citation network as undirected graph and calculate modularity
"""
import sys
import pickle
from igraph import Graph

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

g = Graph.Read_Ncol("data/"+ journal+  "/el_cit", directed=True)
lcc = g.components(mode="WEAK").giant()
vd = lcc.community_walktrap()
cit = vd.as_clustering()
lcc.to_undirected()
# cit = pickle.load(open("results/experiment1/"+journal+".communities_cit.bin", 'rb'))
print("cit net modularity : ", lcc.modularity(cit))
