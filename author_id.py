# size vs strength
import sys

try:
    journal = sys.argv[1]
    pcc_no = sys.argv[2]
    author_count = int(sys.argv[3])
except IndexError:
    print("usage: python3", sys.argv[0], "[jmlr|prl]")
    exit(0)

prefix = journal + ".pcc[" + pcc_no + "].auth["
suffix = "]"
ids = [prefix + str(x +1) + suffix for x in range(author_count)]
print(ids)