#!/usr/bin/python3
'''
    1. get gcc of citation network
    2. get gcc of co-authorship network
    3. detect communities in both of them
    4. replace papers in citation network with corresponding authors
    5. find intersection between the comminities found in both the networks
'''
import sys
import pickle
import clubDetector as cd


try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 experiment3.py [jmlr|prl]")
    exit(0)


def getCommunities(fnam, directed):
    g = cd.input_edgelist(fnam, directed)
    gcc = cd.getLargestConnectedComponent(g)
    communities = cd.detect_communities(gcc, directed)
    if directed:
        pickle.dump(communities, open("./results/experiment1/" + journal + ".communities_cit.bin", 'wb'))
    else:
        pickle.dump(communities, open("./results/experiment1/" + journal + ".communities_co.bin", 'wb'))
    return cd.prepare_output("./data/" + journal + "/" + journal + "_dblp.json", communities, directed)


def filter(comm)->list:
        i = 0
        while i < len(comm):
            if len(comm[i]) < 2:
                comm.pop(i)
            else:
                i += 1
        return comm


if __name__ == '__main__':
    # getting communities
    '''
    c1 = getCommunities("./data/" + journal + "/el_cit", True)
    c2 = getCommunities("./data/" + journal + "/el_co", False)
    # getting clubs
    ''' 
    #uncomment this section for speedup(& comment #L35-36)
    c1 = pickle.load(open("./results/experiment1/" + journal + ".communities_cit.bin", 'rb'))
    c2 = pickle.load(open("./results/experiment1/" + journal + ".communities_co.bin", 'rb'))
    c1 = cd.prepare_output("./data/" + journal + "/" + journal + "_dblp.json", c1, True)
    c2 = cd.prepare_output("NA", c2, False)
    # pruning
    #c1 = filter(c1)
    #c2 = filter(c2)
    # getting communities
    cd.write_communities(c1, "./results/experiment1/" + journal + ".communities_cit.txt")
    cd.write_communities(c2, "./results/experiment1/" + journal + ".communities_co.txt")
    # getting clubs
    c = cd.community_intersection(c1, c2)

    cd.write_clubs(c, './results/experiment1/' + journal + '.clubs.txt')
    cd.write_clubs_bin(c, "./results/experiment1/" + journal + ".clubs.bin")
