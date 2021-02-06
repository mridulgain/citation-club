#!/usr/bin/python3
'''
    All reusable pieces of codes in one file..
    ... cause I messed up with the design.
'''
import pickle
import rawDataParser as rdp
from igraph import Graph
from igraph import VertexClustering


def input_edgelist(fin, directed=True) -> Graph:
    '''
        creates a Graph from the edgelist
    '''
    G = Graph.Read_Ncol(fin, directed=directed, weights=not directed)
    return G


def getLargestConnectedComponent(G: Graph) -> Graph:
    '''
        returns the largest (weakly, in case of directed) connected component
    '''
    weak_components = G.components(mode="WEAK")  # VertexClustering Obj
    largest_weak_component = weak_components.giant()  # Grapg Obj
    return largest_weak_component

# def input_aminer_json


def detect_communities(G: Graph, directed=True) -> VertexClustering:
    """
        input: igraph.Graph Obj
        process: community detection
        output: igraph.VertexClustering Obj
    """
    if directed:
        vertexDendrogram = G.community_walktrap()  # VertexDendrogram obj
        communities = vertexDendrogram.as_clustering()  # VertexClustering Obj
    else:
        communities = G.community_multilevel(weights='weight')
        print("Modularity Score:", communities.modularity)
    # communities = vertexClusters.subgraphs() # List[Graph obj]
    print("No of communities detected :", len(communities))
    return communities


def list_repr_communities(fmap: str, vc: VertexClustering, directed=True) -> list:
    '''
        input:  dblp json file for paper->author mapping
                vertexClustering Obj
                isDirected
        process:
            if directed:
                paper -> author mapping
        output: list(set(authors))
    '''
    com = vc.subgraphs()
    res = []
    if directed:
        # map papers to author
        papers, _ = rdp.load_data(fmap)
        for g in com:
            tmp = set()
            for v in g.vs:
                pid = int(v['name'])  # paper_id
                try:
                    for a in papers[pid]['authors']:
                        tmp.add(int(a['id']))
                except Exception:
                    pass
            res.append(tmp)
    else:
        for g in com:
            tmp = set()
            for v in g.vs:
                tmp.add(int(v['name']))  # author_id
            res.append(tmp)
    return res


def write_communities(c: list, fout: str) -> None:
    f = open(fout, 'w')
    for i in range(len(c)):
        f.write("{}. {}\n".format(i+1, c[i]))
    f.close()


def community_intersection(c1: list, c2: list) -> list:
    '''
        input: two communities
                (generally co-authorship ans citation)
        output: 2d matrix containing 
                intersection of two communities
    '''
    res = [[None for x in c2] for y in c1]
    for i in range(len(c1)):
        for j in range(len(c2)):
            res[i][j] = c1[i].intersection(c2[j])
    return res


def write_clubs(c: list, fout: str) -> None:
    '''
        this method should not be here
    '''
    f = open(fout, 'w')
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] is not None and len(c[i][j]) > 1:
                f.write("({},{}). {}\n".format(i+1, j+1, c[i][j]))
    f.close()


def list_repr_clubs(c: list) -> list:
    '''
        input: 
        output:
    '''
    clubs = []
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] is not None and len(c[i][j]) > 1:
                clubs.append(c[i][j])
    return clubs


def col_wise_union(matrix: list)-> list:
    '''
        input: result of col wise intersection
                of 2 communities
        output: list of pccs 
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    pccs = []
    for i in range(cols):
        tmp = set()
        for j in range(rows):
            tmp.update(matrix[j][i])
        pccs.append(tmp)
    return pccs


def write_clusters(c: list, fout: str) -> None:
    f = open(fout, 'w')
    for i in range(len(c)):
        if len(c[i]) != 0:
            f.write("(*,{}). {}\n".format(i+1, c[i]))
    f.close()


if __name__ == '__main__':
    print("Not to be executed directly")
    print("Run the experiment files instead")
