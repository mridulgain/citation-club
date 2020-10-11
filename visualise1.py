#!/usr/bin/python3
from clubAnalyser import Analysis
# club = [2035876866, 2116836739, 2045157892, 2130181892, 2700953612, 2109954189, 2110501006, 2427243148, 1986033680, 2148022289, 2300711308, 2583656720, 2656283669, 2162752662, 2120348443, 2702409756, 2116155808, 2140714400, 2678872867, 2101279140, 2138722980, 2113276713, 2135302315, 2130712876, 2497095473, 2598605361, 2119739827, 2141326772, 2127632057, 2285338435, 2165888709, 2683781446, 2168176072, 2099379656, 2114357324, 2137603918, 2104512981, 2591117145, 2157689689, 2155265242, 2396073053, 2163103719, 2118530536, 2515560682, 2108673390, 2110230645, 2562268280, 2126599162] # highest eigen vector value club

# club = [
#     183722240, 1981638017, 2100554498, 2717681412, 2298166661, 659530374, 2111596939, 2923204491, 2092877580, 1206765324, 2498491921, 2717986583, 2692648732, 2944302109, 2167404190, 2260861727, 157622691, 328186532, 2691349669, 2806643110, 2114921128, 2121310506, 2279749166, 1690634799, 2289542319, 2282701359, 2221257390, 90224947, 22135093, 2054555191, 1999770807, 2020801783, 2064984895, 2400164672, 2670173377, 2157112897, 2145260995, 297969600, 2735594999, 2079978182, 1982785356, 2152194765, 1969582158, 1973247951, 2168470652, 60139091, 16705875, 2148329557, 2603447383, 2422299352, 2068608856, 2510858842, 243981275, 2021640924, 120651226, 1389458012, 2119641056, 2123304929, 72441953, 2112824674, 1576801125, 691479014, 2086040183, 2528434920, 246708073, 1970391018, 2032102379, 2221004268, 2138495596, 1526086892, 2115118701, 2104401652, 2142932598, 2285762679, 1995962232, 2003447161, 2435751034, 251023228, 1974613367
# ] # highes betweenness 

# club = [
#     2485633537, 177152004, 1972291593, 2661920265, 2312837134, 2165875728, 2655389208, 2158987803, 2100576291, 2130456104, 2108210217, 2097703981, 1604723759, 2313657906, 2168614452, 2006682166, 132303927, 161269817, 1889475642, 2150887997, 2004861503, 2609987651, 24574532, 2309553220, 1981209670, 2619694662, 512556102, 2093953614, 2088212047, 2443967568, 318894673, 2464094287, 2302862425, 242415709, 2161866848, 2619145315, 2128170596, 1566711909, 289005672, 167589996, 2949025389, 2595437681, 1893736562, 1537048691, 2187581557, 2032270973, 1986182274, 1572478601, 371500171, 2096859791, 2038901907, 2189262995, 2101434519, 2116681370, 168172700, 1980701853, 677722270, 2858415774, 1992641199, 2058584252, 2345664702, 1912135871, 2134439617, 2053214915, 2080686788, 2109587139, 2806907591, 2160888527, 2134498512, 2032345308, 139967712, 2098954979, 2148448995, 1111049960, 2108769517, 712415982, 2192737520, 670306551, 2209303800, 2466810105, 2584127737, 2107302653, 2296948990, 284430083, 2468960519, 1982686475, 2048266507, 2165111055, 2171367185, 1273563922, 2042048789, 2632800540, 163924767, 2063782688, 2072849696, 1691279138, 2086114595, 2169650468, 311375655, 2127973671, 2095782188, 2232397101, 2953371951, 2020289842, 1910597427, 2190151475, 2510924085, 135252792, 2118271290, 2037010747, 2882719549, 2012736320, 2105657664, 130200899, 2037866308, 2172053321, 2028784970, 2165695307, 738438988, 2308824398, 2149131086, 2330451, 2397241174, 2063114072, 2291088731, 2142689629, 1133076831, 2040186208, 1904534369, 1960353634, 2009081702, 2522648935, 2080344424, 2127243113, 2328522601, 2737211241, 2121586545, 2133066616, 662855036, 2016539005, 2162369918, 1034661245, 2041520510, 2116332931, 278754694, 2512381318, 2020781963, 1994357136, 2106500497, 1974025617, 1973162899, 2777174945, 2469499809, 1281575332, 2155890085, 36172711, 2077020583, 2103829928, 19414955, 2307616684, 2018810797, 270351283, 2420433332, 2062380982, 2160652726, 1984316343, 2618550202, 2226538938, 2736861629, 2691474368, 2135804864, 2694804417, 2955258819, 2780658116, 155277768, 2231647228, 309515214, 2550150095, 242635728, 301283286, 2122791383, 1856923607, 1982327768, 297432538, 2029583323, 101938652, 738756060, 2095381979, 2148425697, 2160774113, 2122328552, 2148550123, 2277160431, 2778121718, 2007149047, 2233962492, 2167617533
# ] # higheest degree

club = [
    2035876866, 2045157892, 2700953612, 2110501006, 1986033680, 2148022289, 2656283669, 2101279140, 2497095473, 2683781446, 2168176072, 2137603918, 2104512981, 2396073053, 2163103719
] # scc of eigen 

#fin = './data/prl/prl_dblp.json'
fin = './data/jmlr/jmlr_dblp.json'
print(club)
ca = Analysis(club, fin)

#####################################graph drawing###############################################
# ca.visualise("results/induced_subg.gv", engine='circo')
##########################strongly connected components for induced subg#########################
comp, score = ca.get_scc()
for i in range(len(comp)):
    print(comp[i], score[i])
print("Club score: ", sum(score))
