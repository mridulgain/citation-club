#!/usr/bin/python3
'''
    Everything about analysis
    1. collaboration
    2. projection
    3. club citations
    4. journal citaions
'''
import rawDataParser as rdp


class clubAnalyser:
    def __init__(self, db: str):
        '''
            input: dblp aminer json file name
        '''
        self.papers, self.authors = rdp.load_data(db)

    def get_collab(self, club: list) -> list:
        '''
            input:
                club: list of authors
            returns:
                collaboration matrix,
                where matrix(i, j) = no of collab between i & j
        '''
        coauth = [[set() for x in range(len(club))] for y in range(len(club))]
        for i in range(len(club)):
            for j in range(i, len(club)):
                paper_i = self.authors[club[i]]['papers']
                paper_j = self.authors[club[j]]['papers']
                coauth[j][i] = coauth[i][j] = set(paper_i).intersection(paper_j)
        return coauth

    def get_projection(self, club: list) -> list:
        '''
            input:
                club: list of authors
            output:
                projection matrix where,
                each element matrix(i, j): set of citations(a, b) from i to j
                a, b are authored by i & j respectively
        '''
        ref = [[set() for x in range(len(club))] for y in range(len(club))]
        for i in range(len(club)):
            i_papers = self.authors[club[i]]['papers']
            for k in i_papers:
                i_paper_ref = self.papers[k]['references']
                for j in range(len(club)):
                    j_papers = self.authors[club[j]]['papers']
                    tmp = set()
                    for l in set(j_papers).intersection(i_paper_ref):
                        # i cites j with k->l, author(k)=i, author(l)=j
                        tmp.add((k, l))
                    ref[i][j].update(tmp)
        return ref

    def count_journal_cit(self, club: list) -> list:
        '''
            input: list of authors
            output: respective citation count
                total citation for an author
                    = sum(len(cited_by) for all his papers)
        '''
        count = [0] * len(club)
        for i in range(len(club)):
            i_papers = self.authors[club[i]]['papers']
            for p in i_papers:
                count[i] += len(self.papers[p]['cited_by'])
        return count

    def get_club_cit(self, club: list) -> list:
        '''
            input:
                club: list of authors
            returns:
                totatl citation from club =  row wise union of ref matrix )
        '''
        ref = self.get_projection(club)
        cit = [None] * len(club)
        for i in range(len(club)):
            tmp = set()
            for j in range(len(club)):
                tmp.update(ref[j][i])
            cit[i] = tmp
        return cit


if __name__ == '__main__':
    print("Run analysis.py")
