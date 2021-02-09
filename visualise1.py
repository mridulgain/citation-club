#!/usr/bin/python3
from clubAnalyser import Analysis
# club = [2144446980, 2169507332, 2264840197, 2146387448, 68675087, 2140989471, 2509220393, 2273707053, 2105864238, 2510025783, 2309141562, 2158996540, 2150454853, 2168129606, 2228228686, 29156430, 285722199, 2083121761, 2023969377, 2500366947, 2948639857, 2226889331, 1213397108, 112182388, 580814456, 1970964601, 2757437565, 2152748675, 332449412, 2217686667, 2085880977, 1980954773, 2679566486, 46470299, 1992851618, 2127138980, 2288574632, 2144112298, 81068725, 2120199875, 2161922758, 2788039881, 2075486410, 76530380, 2028140240, 1984130259, 2169544406, 2037742808, 1973756125, 2785665251, 2130296053, 2226898200, 2230436637, 2058211624, 222680366, 2576568117, 2193519928, 1911282488, 2155697977, 2792399679, 278134592, 2137021762, 2572083017, 2480733002, 2621583694, 2038168928, 2399628797, 2158748514, 2893478262, 1236609927, 2195679122, 1954235802, 2258767774, 1969841055, 2129265593, 2372578746, 1991817147, 1989832124, 2711419841, 2319292354, 2078454212, 2760752072, 2230476236, 2357163472, 2021011417, 2064393185, 2614831073, 2537523171, 2974200298, 2718390253, 2782238196, 1224875509, 2489391096, 1971726845, 2165532159]
# fin = './data/prl/prl_dblp.json'
club = [2485633537, 177152004, 2661920265, 255084042, 2312837134, 2655389208, 2100576291, 2130456104, 1604723759, 2313657906, 2168614452, 161269817, 1889475642, 2150887997, 2004861503, 2609987651, 2309553220, 24574532, 1981209670, 1988519498, 2443967568, 318894673, 2302862425, 2161866848, 2128170596, 1566711909, 2949025389, 2595437681, 1893736562, 1537048691, 2187581557, 2032270973, 1572478601, 371500171, 2038901907, 2189262995, 2101434519, 2116681370, 168172700, 1980701853, 2058584252, 2345664702, 1912135871, 2053214915, 2080686788, 2109587139, 2806907591, 2160888527, 2134498512, 2032345308, 1111049960, 712415982, 2192737520, 670306551, 2209303800, 2107302653, 284430083, 2632800540, 163924767, 133767967, 2072849696, 2169650468, 2127973671, 1898836778, 2095782188, 2953371951, 2020289842, 1910597427, 2037010747, 2882719549, 2012736320, 2105657664, 130200899, 2037866308, 2172053321, 2028784970, 2308824398, 2149131086, 2397241174, 2063114072, 2291088731, 1904534369, 1960353634, 2522648935, 2080344424, 2328522601, 2133066616, 662855036, 2016539005, 2162369918, 1034661245, 2116332931, 278754694, 2020781963, 2106500497, 1974025617, 1973162899, 2469499809, 1281575332, 2155890085, 36172711, 2077020583, 19414955, 2224929196, 2018810797, 270351283, 2420433332, 2160652726, 2226538938, 2618550202, 2736861629, 2691474368, 2955258819, 2780658116, 309515214, 2122791383, 1856923607, 2029583323, 101938652, 2148425697, 2122328552, 2277160431, 2778121718, 2007149047, 2233962492, 241899517]
fin = './data/jmlr/jmlr_dblp.json'
print(club)
ca = Analysis(club, fin)

#####################################graph drawing###############################################
ca.visualise("results/induced_subg.gv", engine='circo')
##########################strongly connected components for induced subg#########################
sccs = ca.get_scc()
for i in sccs:
    print(i.members, i.weight)
