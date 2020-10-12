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

import sys
import pickle
import clubDetector as cd
from clubAnalyser import Analysis


try:
    journal = sys.argv[1]
except IndexError:
    print("usage: python3 experiment4.py [jmlr|prl]")
    exit(0)


if __name__ == '__main__':
    '''
    # 1
    print('reading edge lists..')
    citnet = cd.input_edgelist("./data/"+journal+"/el_cit", directed = True)
    coauthnet = cd.input_edgelist("./data/"+journal+"/el_co", directed = False)
    # 2
    print('extracting gcc..')
    citnet_gcc = cd.getLargestConnectedComponent(citnet)
    coauthnet_gcc = cd.getLargestConnectedComponent(coauthnet)
    # 3
    print('detecting communities...')
    citnet_comm = cd.detect_communities(citnet_gcc, directed = True)
    coauthnet_comm = cd.detect_communities(coauthnet_gcc, directed = False)
    pickle.dump(citnet_comm,
        open("./results/experiment4/"+journal+".communities_cit.bin", 'wb'))
    pickle.dump(coauthnet_comm,
        open("./results/experiment4/"+journal+".communities_co.bin", 'wb'))
    '''
    #
    # alternatively if you already have communities as .bin file, you can
    # comment out step 1 to 3 and uncomment the following part for speeding up
    # the execution
    #
    
    citnet_comm = pickle.load(
        open("./results/experiment4/"+journal+".communities_cit.bin", 'rb'))
    coauthnet_comm = pickle.load(
        open("./results/experiment4/"+journal+".communities_co.bin", 'rb'))
    
    # 4
    print('mapping papers to authors..')
    cit_comm = cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json",
                                                citnet_comm, directed = True)
    coauth_comm = cd.prepare_output("./data/"+journal+"/"+journal+"_dblp.json",
                                                coauthnet_comm, directed = False)
    # 5
    print('intersecting communities..')
    intersections = cd.community_intersection(cit_comm, coauth_comm)
    cd.write_clubs(intersections, "./results/experiment4/"+journal+".intersection.txt")
    # 6
    print('col wise union...')
    clusters = []
    for i in range(len(coauth_comm)):
        tmp = cd.col_wise_union(i, 'results/experiment4/'+ journal + '.intersection.txt')
        clusters.append(tmp)
    cd.write_clusters(clusters, './results/experiment4/'+journal+'.union.txt')
    # 7
    print('computing scc..')
    db = './data/'+ journal + '/' + journal +'_dblp.json'
    sccs = []
    for c in clusters:
        if len(c) > 0:
            ca = Analysis(list(c), db)
            scc = ca.get_scc()
            sccs.append(scc)
    f = open('./results/experiment4/'+journal+'.scc.txt', 'w')
    for tmp in sccs:
        for scc in tmp:
            if scc.weight != 0:
                f.write("{} ~ {} ~ {}\n".format(scc.members, len(scc.members), scc.weight))
        #f.write('\n')
    f.close()
