'''
    usage: ./experiment4.py [jmlr|prl]
    1. take citation & co-auth net for both journals
    2. compute gcc
    3. detect communities in both net.
    4. map paper to author for cit net. communities
    5. computer intersection between communities
    6. get col. wise union; aka clusters
    7. keep only those scc which has some weight; aka pcc
'''

import pickle
import clubDetector as cd
import sys

try:
    journal = sys.argv[1]
except IndexError:
    print("usage: python3 experiment4.py [jmlr|prl]")
    exit(0)

if __name__ == '__main__':
    # 1
    citnet = cd.input_edgelist("./data/"+journal+"/el_cit", directed = True)
    coauthnet = cd.input_edgelist("./data/"+journal+"/el_co", directed = False)
    # 2
    citnet_gcc = cd.getLargestConnectedComponent(citnet)
    coauthnet_gcc = cd.getLargestConnectedComponent(coauthnet)
    # 3
    citnet_comm = cd.detect_communities(citnet_gcc, directed = True)
    coauthnet_comm = cd.detect_communities(coauth_gcc, directed = False)
    pickle.dump(citnet_comm,
        open("./results/experiment4/"+journal+".communities_cit.bin", 'wb'))
    pickle.dump(coauthnet_comm,
        open("./results/experiment4/"+journal+".communities_co.bin", 'wb'))
    #
    # alternatively if you already have communities as .bin file, you can
    # comment out step 1 to 3 and uncomment the following part for speeding up
    # the execution
    #
    '''
    citnet_comm = pickle.load(
        open("./results/experiment4/"+journal+".communities_cit.bin", 'rb'))
    coauthnet_comm = pickle.load(
        open("./results/experiment4/"+journal+".communities_co.bin", 'rb'))
    '''
    # 4
    c1 = cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json",
                                                citnet_comm, directed = True)
    c2 = cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json",
                                                coauthnet_comm, directed = False)
    # 5
    tmp = cd.community_intersection(c1, c2)
    cd.write_clubs(tmp, "./results/experiment4/"+journal+".intersection.txt")
    # 6
    clusters = []
    for i in range(len(c2)):
        tmp = cd.col_wise_union(i, 'results/experiment4/'+ journal + '.intersection.txt')
        clusters.append(tmp)
    cd.write_clusters(clusters, './results/experiment4/'+journal+".union.txt")
