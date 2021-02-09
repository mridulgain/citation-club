# centrality calculation
import sys
import pickle
import clubDetector as cd

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

g = cd.input_edgelist("data/" + journal + "/el_co", directed=False)
gcc = cd.getLargestConnectedComponent(g)

# eigen vector centrality
evc = gcc.evcent(directed=False, weights='weight')
# betweenness centrality
bc = gcc.betweenness(directed=False, weights='weight')
# degree
dc = gcc.degree()

#print(max(evc))
print(gcc.vs[evc.index(max(evc))])
print(gcc.vs[bc.index(max(bc))])
print(gcc.vs[dc.index(max(dc))])
print(max(dc))