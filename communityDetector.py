#!/usr/bin/python3
import pickle
import rawDataParser as rdp
from igraph import Graph
from igraph import VertexClustering


def input_edgelist(fin="graph.ncol", directed=True) -> Graph:
    '''
        Input: A graph in edgelist file
        process: getting gcc
        Output: igraph.Graph obj
    '''
    G = Graph.Read_Ncol(fin, directed=directed, weights=not directed)
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


def prepare_output(communities: VertexClustering, directed=True) -> list:
    '''
        input: vertexClustering Obj
        process:
            if directed:
                paper -> author mapping
        output: list(set(authors))
    '''
    com = communities.subgraphs()
    res = []
    if directed:
        # map papers to author
        papers, authors = rdp.load_data("./data/prl_dblp_5335.json")
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


def community_intersection(c1: list, c2: list) -> list:
    res = [[None for x in c2] for y in c1]
    for i in range(len(c1)):
        for j in range(len(c2)):
            res[i][j] = c1[i].intersection(c2[j])
    return res


if __name__ == '__main__':
    print("Not to be executed directly")
    print("Run the experiment files instead")
