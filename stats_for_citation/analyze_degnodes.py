# get list of coauthors
# get total citations [out degree]
# get total references [in degree]
# get clubs
# get club citations

import pandas as pd
import json
from in_data import in_data_file

data = json.load(open('../../analysis/data/data.json'))


def papers(auth_id):
    papers_list = []
    for element in data:
        for ele in element['authors']:
            if auth_id == ele['id']:
                papers_list.append(element['id'])   
    return papers_list

   
def coauth_paper(paper_id):
    coauth = {}
    for element in data:
        if element['id'] == paper_id:
            coauth[element['id']] = element['authors']
    if len(coauth) >= 1:
        return coauth
    else:
        return None


def coauthors(auth_id):

    coauth = {}
    for element in data:
            for ele in element['authors']:
                if auth_id == ele['id']:
                    coauth[element['id']] = element['authors']
    if len(coauth) >= 1:
        return coauth



def citations(auth_id, papers_list):
    cits = {}
    cit_auth = []

    for element in data:
        if element['id'] in papers_list:
            try:
                cits[element['id']] = [element['references'], element['n_citation']]
                for ele in element['references']:
                    cit_auth.append(coauth_paper(ele))
            except:
                pass
    return cits, cit_auth


def get_clubs(auth_id):
    clubs = []
    with open('../../experiment1/jmlr.clubs.txt') as club_file:
        for line in club_file.readlines():

            temp = line.rstrip().replace(" ", "").replace("{", "").replace("}", "").split('.')
            temp2 = temp[1].rstrip().replace("\n", "").split(",")
            temp3 = [int(x) for x in temp2]
            if auth_id in temp3:
                clubs.append(temp3) 
    return clubs

def get_references(papers_):
    references = {}
    ref_auth = []
    for paper in papers_:
        for element in data:
            try:
                if paper in element['references']:
                    references[paper] = element['id']
                    ref_auth.append(coauth_paper(element['id']))
            except Exception as e:
                pass
    return references, ref_auth

def get_ids_from_citauth(auth_id, all_data):
    list_cit_coauth = []
    for element in all_data[auth_id]['citation_coauth']:
        if element is not None:
            for ele in element.values():
                for e in ele:
                    # print(e['id'])
                    list_cit_coauth.append(e['id'])
    return(list_cit_coauth)
    
def number_club_citations(cit_auth, club_auth, all_data):
    # print(cit_auth)
    sum_ = 0
    for element in club_auth:
        for ele in element:
            if ele in cit_auth:
                sum_ += 1
                # print("Club", ele)
    # print(sum_)
    return sum_

def number_total_citations(auth_id, all_data):
    sum_ = len(all_data[auth_id]['ref_auth'])
    return sum_

def calculate_all(value):
    all_data = {}
    for i in range(5):
        # print(value.iloc[i][0])
        papers_list = papers(value.iloc[i][0])
        c = coauthors(value.iloc[i][0])
        a, b = citations(value.iloc[i][0], papers_list)
        cl = get_clubs(value.iloc[i][0])
        r, ra = get_references(papers_list)
        all_data[str(value.iloc[i][0])] = {'coauthors': c, 'citations': a, 'citation_coauth': b, 'clubs': cl, 'references': r, 'ref_auth': ra}
        club_cit = number_club_citations(get_ids_from_citauth(str(value.iloc[i][0]), all_data), cl, all_data)
        jour_cit = number_total_citations(str(value.iloc[i][0]), all_data)
        all_data[str(value.iloc[i][0])].update({'club_citation': club_cit, 'journal_citations': jour_cit})
        # break
    # print(all_data.values())

    data_json = json.dumps(all_data)
    print(data_json)





'''
def calculate(values):
    all_data = {}
    for i in values:
        # print(value.iloc[i][0])
        papers_list = papers(i)
        c = coauthors(i)
        a, b = citations(i, papers_list)
        cl = get_clubs(i)
        r, ra = get_references(papers_list)
        all_data[str(i)] = {'coauthors': c, 'citations': a, 'citation_coauth': b, 'clubs': cl, 'references': r, 'ref_auth': ra}
        club_cit = number_club_citations(get_ids_from_citauth(str(i), all_data), cl, all_data)
        jour_cit = number_total_citations(str(i), all_data)
        all_data[str(i)].update({'club_citation': club_cit, 'journal_citations': jour_cit})
        # break
    # print(all_data.values())
    data_json = json.dumps(all_data)
    print(data_json)

# values = [179778838,92438100,1963576484,2148425697,	2467740887,	2150527135,] # degree 20
# values = [134769616,563069026,2619985137,2100767082,2038901907] # degree 10
# values =[2609987651, 2122328552, 1972291593, 1572478601, 2038901907, 60139091, 297432538, 168172700, 1980701853]
# calculate(values)
'''


### uncomment and run.
# deg_coauth = pd.read_csv('../../analysis/degreenodes_graph/degree_coauth.csv')
# ei_coauth =  pd.read_csv('../../analysis/degreenodes_graph/eigen_coauth.csv')
# btw_coauth =  pd.read_csv('../../analysis/degreenodes_graph/between_coauth.csv')
# sort_deg_coauth = deg_coauth.sort_values(by=['x'], ascending = False).head(5)
# sort_ei_coauth = ei_coauth.sort_values(by=['vector'], ascending = False).head(5)
# sort_btw_coauth = btw_coauth.sort_values(by=['x'], ascending = False).head(5)
# calculate_all(sort_deg_coauth)
# calculate_all(sort_ei_coauth)
# calculate_all(sort_btw_coauth)






'''For papers will improve later'''
'''for papers
get coauthors
get clubs
get citations (out degree)
get references (in degree)
'''

def pre_processing_for_cit(df):
    li = df.head(80).to_dict()
    new_lis = {v:k for k,v in li['Unnamed: 0'].items()}
    li = in_data_file(new_lis, li)
    new_li = {x:y for x,y in zip(list(li.keys())[:10], list(li.values())[:10])}
    return new_li

def after_coauth(auth):
    # print(auth)
    au = []
    for ele in auth.values():
        for e in ele:
            au.append(e['id'])
    return au

def get_club_cit_paper(club_auth, cit_auth):
    # print(club_auth)
    # print(cit_auth)
    sum_ = 0
    for element in cit_auth:
        if element is not None:
            # print(list(element.values())[0])
            for ele in list(element.values())[0]:
                if ele['id'] in club_auth:
                    # print(ele['id'])
                    sum_ += 1
    return sum_

def get_jour_cit(auth, all_data_papers, pap_id):
    return len(list(all_data_papers[str(pap_id)]['ref_auth'].values())[0])

def calculate_all_papers(paper_values):
    # all_data[str(value.iloc[i][0])] = {'coauthors': c, 'citations': a, 'citation_coauth': b, 'clubs': cl, 'references': r, 'ref_auth': ra}
    # print(paper_values)
    all_data_papers = {}
    for paper_id in list(paper_values.keys()):
        coauth = coauth_paper(paper_id)
        club = {}
        citation = {}
        cit_auth = {}
        r , ra = {}, {}
        all_data_papers[str(paper_id)] = {'degree': paper_values[paper_id] , 'coauthors': coauth}
        au = after_coauth(coauth)
        pap_au = {}
        for a in au:
            pap_au[a] = papers(a)
            club[a] = get_clubs(a)
            citation[a], cit_auth[a] = citations(a, pap_au[a])
            r[a], ra[a] = get_references(list(pap_au.values())[0])
        all_data_papers[str(paper_id)].update({'club': club, 'citations': citation, 'citation_coauth': cit_auth, 'references': r, 'ref_auth': ra})

        club_cit = {}
        jour_cit = {}
        for a in au:
            club_cit[a] = get_club_cit_paper(club[a][0], cit_auth[a])
            jour_cit[a] = get_jour_cit(a, all_data_papers, paper_id)
        all_data_papers[str(paper_id)].update({'club_citation': club_cit, 'journal_citations': jour_cit})


        



        
    data_json = json.dumps(all_data_papers)
    # print(data_json)
    return(data_json)


ei_cit =  pd.read_csv('../../analysis/degreenodes_graph/eigen_cit.csv').sort_values(by=['vector'], ascending = False)
btw_cit =  pd.read_csv('../../analysis/degreenodes_graph/between_cit.csv').sort_values(by=['x'], ascending = False)
deg_cit = pd.read_csv('../../analysis/degreenodes_graph/degree_cit.csv').sort_values(by=['x'], ascending = False)


final_deg_dict = pre_processing_for_cit(deg_cit)
final_ei_dict = pre_processing_for_cit(ei_cit)
final_btw_dict = pre_processing_for_cit(btw_cit)

# print(final_deg_dict)
value = calculate_all_papers(final_deg_dict)
print(value)
# ['1647376582']