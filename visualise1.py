#!/usr/bin/python3
from clubAnalyser import Analysis
#club = [2064393185, 2120199875, 2078454212, 2150454853, 2309141562, 76530380, 1969841055, 2195679122, 2146387448, 1954235802, 2258767774, 2165532159]
club = [2035876866, 2116836739, 2130181892, 2700953612, 2300711308, 2110501006, 2583656720, 2162752662, 2120348443, 2140714400, 2138722980, 2113276713, 2135302315, 2130712876, 2598605361, 2119739827, 2141326772, 2127632057, 2165888709, 2168176072, 2114357324, 2591117145, 2157689689, 2155265242, 2396073053, 2118530536, 2108673390, 2110230645, 2126599162]
#fin = './data/prl/prl_dblp.json'
fin = './data/jmlr/jmlr_dblp.json'
print(club)
ca = Analysis(club, fin)

#####################################graph drawing###############################################
ca.visualise("results/induced_subg.gv", engine='circo')
##########################strongly connected components for induced subg#########################
comp, score = ca.get_scc()
for i in range(len(comp)):
    print(comp[i], score[i])
print("Club score: ", sum(score))
