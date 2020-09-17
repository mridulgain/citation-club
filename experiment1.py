#!/usr/bin/python3
'''
    1. get gcc of citation network
    2. get gcc of co-authorship network
    3. detect communities in both of them
    4. replace papers in citation network with corresponding authors
    5. find intersection between the comminities found in both the networks
'''
import pickle
import clubDetector as cd


def getCommunities(fnam, directed):
    g = cd.input_edgelist(fnam, directed)
    gcc = cd.getLargestConnectedComponent(g)
    communities = cd.detect_communities(gcc, directed)
    if directed:
        pickle.dump(communities, open("./data/jmlr/communities_cit.bin", 'wb'))
    else:
        pickle.dump(communities, open("./data/jmlr/communities_co.bin", 'wb'))
    return cd.prepare_output("./data/jmlr/jmlr_dblp.json", communities, directed)


if __name__ == '__main__':
    '''# getting communities
    c1 = getCommunities("./data/jmlr/el_cit", True)
    c2 = getCommunities("./data/jmlr/el_co", False)
    # getting clubs'''
    c1 = pickle.load(open("./data/jmlr/communities_cit.bin", 'rb'))
    c2 = pickle.load(open("./data/jmlr/communities_co.bin", 'rb'))
    c1 = cd.prepare_output("./data/jmlr/jmlr_dblp.json", c1, True)
    c2 = cd.prepare_output("NA", c2, False)
    # getting communities
    cd.write_communities(c1, "./data/jmlr/communities_cit.txt")
    cd.write_communities(c2, "./data/jmlr/communities_co.txt")
    # getting clubs
    c = cd.community_intersection(c1, c2)
    cd.write_clubs(c, './data/jmlr/clubs.txt')
