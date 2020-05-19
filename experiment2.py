#!/usr/bin/python3
import clubDetector as cd
import pickle


def getComponents(fnam, directed=False):
    g = cd.input_edgelist(fnam, directed)
    components = g.components()
    return components


if __name__ == '__main__':
    '''# getting communities
    c1 = getCommunities("./data/jmlr/el_cit", True)
    c2 = getCommunities("./data/jmlr/el_co", False)
    # getting clubs'''
    c1 = pickle.load(open("./data/prl/communities_cit.bin", 'rb'))
    c2 = getComponents("./data/prl/el_co", False)
    c1 = cd.prepare_output("./data/prl/prl_dblp.json", c1, True)
    c2 = cd.prepare_output("s", c2, False)
    cd.write_communities(c1, "./data/prl/communities_cit.txt")
    cd.write_communities(c2, "./data/prl/communities_co.txt")
    c = cd.community_intersection(c1, c2)
    cd.write_clubs(c, './data/prl/clubs.txt')
