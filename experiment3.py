#!/usr/bin/python3
'''
    same as experiment1
    except taking whole graph instead of gcc for co-authorship network
'''
import pickle
import clubDetector as cd


def getCommunities(fnam, directed):
    g = cd.input_edgelist(fnam, directed)
    if directed:
        gcc = cd.getLargestConnectedComponent(g)
    else:
        gcc = g
    communities = cd.detect_communities(gcc, directed)
    ###
    if directed:
        pickle.dump(communities, open("./results/experiment3/prl.communities_cit.bin", 'wb'))
    else:
        pickle.dump(communities, open("./results/experiment3/prl.communities_co.bin", 'wb'))
    ###
    return cd.prepare_output("./data/prl/prl_dblp.json", communities, directed)

if __name__ == '__main__':
    # getting communities
    c1 = getCommunities("./data/prl/el_cit", True)
    c2 = getCommunities("./data/prl/el_co", False)
    # getting clubs
    cd.write_communities(c1, "./results/experiment3/prl.communities_cit.txt")
    cd.write_communities(c2, "./results/experiment3/prl.communities_co.txt")
    c = cd.community_intersection(c1, c2)
    cd.write_clubs(c, './results/experiment3/prl.clubs.txt')
