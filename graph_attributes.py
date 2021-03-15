#
import sys
import pickle
from igraph import Graph


def attributes(g)->None:
    lcc = g.components(mode="WEAK").giant()
    print("Nodes & edges", len(lcc.vs), len(lcc.es))

if __name__ == '__main__':
    try:
        journal = sys.argv[1]
    except IndexError:
        #journal = "prl"
        print("usage: python3", sys.argv[0], "[jmlr|prl]")
        exit(0)
    print("cit net :")
    cit_g = Graph.Read_Ncol("data/"+ journal+  "/el_cit", directed=True)
    attributes(cit_g)
    print("coauth net :")
    coauth_g = Graph.Read_Ncol("data/"+ journal+  "/el_co", directed=False)
    attributes(coauth_g)