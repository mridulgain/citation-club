#!/usr/bin/python3
'''
    helping methods to parse dblp json file
'''
import json


def get_papers(data: list) -> dict:
    '''
    hashing paper entries wrt paper_id
    keys:  title, authors, n_citations, & references, cited_by
    '''
    d = {}
    for i in data:
        ref = i['references'] if 'references' in i else []
        if i['id'] not in d:
            d[i['id']] = {
                            'title': i['title'],
                            'authors': i['authors'],
                            'n_citation': i['n_citation'],
                            'references': ref,
                            'cited_by': []
                        }
        d[i['id']]['title'] = i['title']
        d[i['id']]['authors'] = i['authors']
        d[i['id']]['n_citation'] = i['n_citation']
        d[i['id']]['references'] = ref
        for r in ref:
            if r not in d:
                d[r] = {
                            'title': i['title'],
                            'authors': i['authors'],
                            'n_citation': i['n_citation'],
                            'references': ref,
                            'cited_by': []
                        }
            d[r]['cited_by'].append(i['id'])
    return d


def get_authors(data: list) -> dict:
    '''
    hashing authors wrt author_id
    keys : name, org, papers
    '''
    d = {}
    for i in data:
        paper = i['id']
        authors = i['authors']
        for j in authors:
            ID = j['id']
            name = j['name'] if 'name' in j else ""
            # org = j['org'] if 'org' in j else None
            if ID not in d:
                d[ID] = {
                            'name': set(),
                            'papers': list()
                        }
            d[ID]['name'].add(name)
            d[ID]['papers'].append(paper)
    return d


def read_json(fin: str) -> list:
    f = open(fin, 'r')
    data = json.load(f)  # file -> ds
    return data


def load_data(fin="./data/prl/prl_dblp.json"):
    '''
    format : list(dict)
    dict.keys():'fos', 'alias_ids', 'volume', 'id', 'page_end',
                'venue', 'authors', 'references', 'year', 'doi', 'page_start',
                'issue', 'n_citation', 'publisher', 'title', 'doc_type',
                'indexed_abstract'
    returns : papers, authors
    '''
    data = read_json(fin)
    return get_papers(data), get_authors(data)


def get_collab(club: list, fin: str) -> list:
    '''
        input:
            club: list of authors
            fin: dblp aminer json
        output:
            collaboration matrix, where matrix(i, j) = no of collab between i & j
    '''
    papers, authors = load_data(fin)
    coauth = [[set() for x in range(len(club))] for y in range(len(club))]
    for i in range(len(club)):
        for j in range(i, len(club)):
            paper_i = authors[club[i]]['papers']
            paper_j = authors[club[j]]['papers']
            coauth[j][i] = coauth[i][j] = set(paper_i).intersection(paper_j)
    return coauth


def get_projection(club: list, fin: str) -> list:
    '''
        input:
            club: list of authors
            fin: dblp aminer json
        output:
            collaboration matrix, where matrix(i, j) = no of collab between i & j
    '''

if __name__ == '__main__':
    print('run the clubAnalyser.py or experiment*.py files')
