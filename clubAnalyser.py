#!/usr/bin/python3
'''
    Everything about analysis
    1. collaboration
    2. projection
    3. club citations
    4. journal citaions
'''
import rawDataParser as rdp
from graphviz import Digraph
from igraph import Graph


class Analysis:
    def __init__(self, club, db: str):
        '''
            input: dblp aminer json file name
        '''
        self.members = club
        self.papers, self.authors = rdp.load_data(db)
        self.collab = self.get_coauth_matrix()
        self.projection = self.get_reference_matrix()

    def get_coauth_matrix(self) -> list:
        '''
            input:
                club: list of authors
            returns:
                collaboration matrix,
                where matrix(i, j) = set of paper published by i & j togather
        '''
        club = self.members
        coauth = [[set() for x in range(len(club))] for y in range(len(club))]
        for i in range(len(club)):
            for j in range(i, len(club)):
                paper_i = self.authors[club[i]]['papers']
                paper_j = self.authors[club[j]]['papers']
                coauth[i][j] = set(paper_i).intersection(paper_j)
                coauth[j][i] = coauth[i][j]
        return coauth

    def get_reference_matrix(self) -> list:
        '''
            input:
                club: list of authors
            output:
                projection matrix where,
                each element matrix(i, j): set of citations(a, b) from i to j
                a, b are authored by i & j respectively
        '''
        club = self.members
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

    def count_journal_cit(self) -> list:
        '''
            input: list of authors
            output: respective citation count
                total citation for an author
                    = sum(len(cited_by) for all his papers)
        '''
        club = self.members
        count = [0] * len(club)
        for i in range(len(club)):
            i_papers = self.authors[club[i]]['papers']
            for p in i_papers:
                count[i] += len(self.papers[p]['cited_by'])
        return count

    def get_club_cit(self) -> list:
        '''
            input:
                club: list of authors
            returns:
                totatl citation from club =  row wise union of ref matrix )
        '''
        club = self.members
        ref = self.projection
        cit = [None] * len(club)
        for i in range(len(club)):
            tmp = set()
            for j in range(len(club)):
                tmp.update(ref[j][i])
            cit[i] = tmp
        return cit

    def visualise(self, fout="tmp.gv", engine='dot', format='pdf') -> None:
        coauth = self.collab
        ref = self.projection
        club = self.members
        g = Digraph(comment="induced sub graph", format=format, engine=engine)
        for i in club:
            g.node(str(i))
        with g.subgraph(name='coauth') as c:
            c.attr('edge', dir='none', color='red')
            for i in range(len(club)):
                for j in range(i, len(club)):
                    if i != j and len(coauth[i][j]) > 0:
                        c.edge(str(club[i]), str(club[j]), label=str(len(coauth[i][j])))
        with g.subgraph(name='cit') as c:
            for i in range(len(club)):
                for j in range(len(club)):
                    if len(ref[i][j]) > 0:
                        g.edge(str(club[i]), str(club[j]), label=str(len(ref[i][j])))
        g.render(fout, view=True)

    def strongly_connected_components(self) -> list:
        club = self.members
        ref = self.projection
        g = Graph(directed=True)
        for i in club:
            g.add_vertex(name=i)
        for i in range(len(club)):
            for j in range(len(club)):
                if len(ref[i][j]) > 0:
                    g.add_edge(i, j, weights=len(ref[i][j]))
        print("total weight", sum(g.es['weights']))
        scc = g.components(mode='STRONG').subgraphs()
        for ix, c in enumerate(scc):
            score = sum(c.es['weights'])
            tmp = []
            for v in c.vs:
                tmp.append(v['name'])
            print(tmp, "score ", score)


if __name__ == '__main__':
    print("Run analysis.py or visualise.py")
