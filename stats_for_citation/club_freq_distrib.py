import sys
import matplotlib.pyplot as plt

try:
    journal = sys.argv[1]
except IndexError:
    #journal = "prl"
    print("usage: python3 club_freq_distrib.py [jmlr|prl]")
    exit(0)

fnam = "../results/experiment1/" + journal + ".clubs.txt"

freq = {}
member = []
with open(fnam, "r") as file:
    for line in file:
        key = len(line.split()) - 1
        '''
        if key == 86:
            print(line)'''
        freq[key] = freq.setdefault(key, 0) + 1
        member.append(key)
print(freq)
#print(member)
#print(sum(freq.values()))
#plt.hist(member)
#plt.show()
'''
for i in freq:
    print(i, ",", freq[i])'''