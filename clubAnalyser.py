#!/usr/bin/python3
import rawDataParser as rdp

# club = [2608506984, 2163830057, 2106866729, 2639260782, 2299437103, 2079150322, 2110542169, 2593217274, 2907377662]
club = [2609987651, 2122328552, 1972291593, 1572478601, 2038901907, 60139091, 297432538, 168172700, 1980701853]
print(club)
# papers, authors = rdp.load_data('./data/prl/prl_dblp.json')
papers, authors = rdp.load_data('./data/jmlr/jmlr_dblp.json')

# co authorship matrix formation
coauth = [[set() for x in range(len(club))] for y in range(len(club))]
for i in range(len(club)):
    for j in range(i, len(club)):
        paper_i = authors[club[i]]['papers']
        paper_j = authors[club[j]]['papers']
        coauth[j][i] = coauth[i][j] = set(paper_i).intersection(paper_j)
# output
print("Coauthorship count-------------------------------------------")
for i in range(len(club)):
    for j in range(len(club)):
        print(len(coauth[i][j]), end=" | ")
    print("\n")
print("Coauthorship details-----------------------------------------")
for i in range(len(club)):
    for j in range(len(club)):
        print(coauth[i][j], end=" | ")
    print("\n")

# reference count
ref = [[set() for x in range(len(club))] for y in range(len(club))]
for i in range(len(club)):
    i_papers = authors[club[i]]['papers']
    for k in i_papers:
        i_paper_ref = papers[k]['references']
        for j in range(len(club)):
            j_papers = authors[club[j]]['papers']
            tmp = set()
            for l in set(j_papers).intersection(i_paper_ref):
                # i cites j with k->l, author(k)=i, author(l)=j
                tmp.add((k, l))
            ref[i][j].update(tmp)
# output
print("Citation details :---------------------------------------- ")
for i in range(len(club)):
    for j in range(len(club)):
        print(ref[i][j], end=" | ")
    print("\n")
print("Citation count :---------------------------------------- ")
for i in range(len(club)):
    for j in range(len(club)):
        print(len(ref[i][j]), end=" | ")
    print("\n")
# total citation from journal
n_cit = [0] * len(club)
for i in range(len(club)):
    i_papers = authors[club[i]]['papers']
    for p in i_papers:
        n_cit[i] += len(papers[p]['cited_by'])
print("Total citation from journal:---------------------------------")
for x in zip(club, n_cit):
    print(x)
# totatl citation from club
n_cit_club = [0] * len(club)
for i in range(len(club)):
    for j in range(len(club)):
        n_cit_club[i] += len(ref[j][i])
print("Totalo citation from club:-----------------------------------")
for x in zip(club, n_cit_club):
    print(x)
