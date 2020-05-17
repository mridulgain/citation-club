#!/usr/bin/python3
import rawDataParser as rdp

club = [2106866729, 2163830057, 2593217274, 2110542169, 2639260782, 2299437103]
print(club)
papers, authors = rdp.load_data('./data/prl_dblp_5335.json')

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
            ref[i][j].update(set(j_papers).intersection(i_paper_ref))
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
