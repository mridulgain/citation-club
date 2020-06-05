#!/usr/bin/python3
'''
    same as experiment1
    except taking whole graph instead of gcc for co-authorship network
'''
import pickle
import clubDetector as cd

journal = "jmlr"

def getCommunities(fnam, directed):
    g = cd.input_edgelist(fnam, directed)
    if directed:
        gcc = cd.getLargestConnectedComponent(g)
    else:
        gcc = g
    communities = cd.detect_communities(gcc, directed)
    ###
    if directed:
        pickle.dump(communities, open("./results/experiment3/"+journal+".communities_cit.bin", 'wb'))
    else:
        pickle.dump(communities, open("./results/experiment3/"+journal+".communities_co.bin", 'wb'))
    ###
    return cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json", communities, directed)


def getCommunitiesFromFiles(fnam, directed):
    communities = pickle.load(open(fnam, 'rb'))
    return cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json", communities, directed)


def filter(comm)->list:
        i = 0
        while i < len(comm):
            if len(comm[i]) < 4:
                comm.pop(i)
            else:
                i += 1
        return comm

if __name__ == '__main__':
    '''# getting communities
    c1 = getCommunities("./data/"+journal+"/el_cit", True)
    c2 = getCommunities("./data/"+journal+"/el_co", False)
    # getting clubs
    cd.write_communities(c1, "./results/experiment3/"+journal+".communities_cit.txt")
    cd.write_communities(c2, "./results/experiment3/"+journal+".communities_co.txt")'''
    c1 = getCommunitiesFromFiles("./results/experiment3/"+journal+".communities_cit.bin", True)
    c2 = getCommunitiesFromFiles("./results/experiment3/"+journal+".communities_co.bin", False)
    print("before pruning", len(c1), len(c2))
    c1 = filter(c1)
    c2 = filter(c2)
    print("after pruning", len(c1), len(c2))
    c = cd.community_intersection(c1, c2)
    #print(c)
    print(len(c))
    cd.write_clubs(c, './results/experiment3/'+journal+'.clubs.txt')
