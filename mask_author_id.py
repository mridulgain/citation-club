import sys
import pickle


def search_author(pccs, author)-> int:
    for i, x in enumerate(pccs):
        if author in x[0]:
            return i
    return -1


def mask_author(journal, pccs, pcc_index, author):
    author_index = str(list(pccs[pcc_index][0]).index(author) + 1)
    return journal+".pcc.["+str(pcc_index+1)+"].auth["+author_index+"]"


def mask_club(journal, pccs, pcc_index):
    tmp = []
    for j in range(len(pccs[pcc_index][0])):
        tmp.append(journal+".pcc.["+str(pcc_index+1)+"].auth["+str(j+1)+"]")
    return tmp


if __name__ == "__main__":
    try:
        journal = sys.argv[1]
        author = int(sys.argv[2])
    except IndexError:
        #journal = "prl"
        print("usage: python3 experiment3.py [jmlr|prl] [author_id]")
        exit(0)

    pccs = pickle.load(open("./results/experiment1/" + journal + ".pcc_details.bin", 'rb'))

    if journal == "prl":
        journal = "cj"
    else:
        journal = "oj"

    print(mask_author(journal, pccs, search_author(pccs, author), author))
    #print(mask_club(author))
