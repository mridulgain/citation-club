#!/usr/bin/python3
'''
    1. get gcc of citation network
    2. get gcc of co-authorship network
    3. detect communities in both of them
    4. replace papers in citation network with corresponding authors
    5. find intersection between the comminities found in both the networks
'''
import pickle
import communityDetector as cd


def getCommunities(fnam, directed):
    g = cd.input_edgelist(fnam, directed)
    communities = cd.detect_communities(g, directed)
    if directed:
        pickle.dump(communities, open("./data/communities_cit.bin", 'wb'))
    else:
        pickle.dump(communities, open("./data/communities_co.bin", 'wb'))
    return cd.prepare_output(communities, directed)


if __name__ == '__main__':
    # getting communities
    c1 = getCommunities("./data/el_cit", True)
    c2 = getCommunities("./data/el_co", False)
    # getting clubs
    c = cd.community_intersection(c1, c2)
    f = open("test", 'w')
    for i in c:
        for j in i:
            if len(j) != 0:
                f.write(str(j)+"\n")
    f.close()
