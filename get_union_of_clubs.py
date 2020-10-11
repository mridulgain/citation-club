## pass coauthorship community number as command line argument
def get_list(number):
    values = []
    path = '/home/nandini/Downloads/prl.clubs.txt'
    new_list = []
    with open(path) as f:
        for line in f.readlines():
            line = line.replace("(", "").replace(")", "").replace("{","").replace("}", "")
            # print(line)
            new_line = []
            new_line.extend(line.rstrip().split(". "))
            # print(new_line)
            temp = []
            for y in new_line:
                temp.extend([int(x) for x in y.split(",")])
            new_list.append(temp)
            # print(new_list)
            # break
    for ele in new_list:
        if ele[1] == number:
            values.extend(ele[2:])
    return(values)

import sys
# i = int(sys.argv[1])
for i in range(1500):
    x = get_list(i)
    s = set(x)
    print(i, s, len(s))
