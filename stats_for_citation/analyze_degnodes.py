# how to run the file
# uncomment the dataframe lines or list of ids and call the respective calculate function
# in the console, python3 analyze_degnodes.py > path_to_json_file 

# change line 84
# change line 14, 15, 

import pandas as pd
import json



# calculates if paper is in journal or not
path = '../../analysis/'
data = json.load(open(path+'data/data.json'))

def in_data_file(list_, new_li):
    # print(list_)
    li = list(list_.keys())
    list_of_papers = {}
    data = json.load(open(path+'data/data.json'))
    for id in li:
        for element in data:
            if id == element['id']:
                # print(id, list_[id])
                try:
                    list_of_papers[id] = new_li['x'][list_[id]]
                except:
                    list_of_papers[id] = new_li['vector'][list_[id]]
                break
    return list_of_papers


# gets list of paper ids written by author id
def papers(auth_id):
    papers_list = []
    for element in data:
        for ele in element['authors']:
            if auth_id == ele['id']:
                papers_list.append(element['id'])   
    return papers_list

   
# gets coauthors (dictonary paper_id: [coauth details]) of the given paper
def coauth_paper(paper_id):
    coauth = {}
    for element in data:
        if element['id'] == paper_id:
            coauth[element['id']] = element['authors']
    if len(coauth) >= 1:
        return coauth
    else:
        return None


# gets all coautors of the author. [degree value in colaaboration network]
def coauthors(auth_id):
    coauth = {}
    for element in data:
            for ele in element['authors']:
                if auth_id == ele['id']:
                    coauth[element['id']] = element['authors']
    if len(coauth) >= 1:
        return coauth



# gets the paper ids and author ids of the paper's citation [out degree] of a given author. 
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


# gets all the clubs a author is in
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

# gets a list of all papers and their authors who have cited a particular paper [in degree]
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


# gets author ids from all the citation coauthors of a given author
def get_ids_from_citauth(auth_id, all_data):
    list_cit_coauth = []
    for element in all_data[auth_id]['citation_coauth']:
        if element is not None:
            for ele in element.values():
                for e in ele:
                    list_cit_coauth.append(e['id'])
    return(list_cit_coauth)
    

# gets total number of citations obtained fron the club
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


# ets total number of citation from the journal papers
def number_total_citations(auth_id, all_data):
    sum_ = len(all_data[auth_id]['ref_auth'])
    return sum_


# main function which calculates the parameters for a given set of author ids [dataframe] and returns a json variable
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

# same as calculate_all but here the input in a list of author ids
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


# checks whether a paper is in the journal or not
def pre_processing_for_cit(df):
    li = df.head(80).to_dict()
    new_lis = {v:k for k,v in li['Unnamed: 0'].items()}
    li = in_data_file(new_lis, li)
    new_li = {x:y for x,y in zip(list(li.keys())[:10], list(li.values())[:10])}
    return new_li

# returns just a list of coauthor ids of a given author id. to be run after calling coauth_paper()
def after_coauth(auth):
    # print(auth)
    au = []
    for ele in auth.values():
        for e in ele:
            au.append(e['id'])
    return au

# gets club citations for a paper
def get_club_cit_paper(club_auth, cit_auth):
    # print(len(club_auth))
    # print(club_auth)
    # print(cit_auth)
    sum_ = 0
    for element in cit_auth:
        if element is not None:
            # print(list(element.values())[0])
            for ele in list(element.values())[0]:
                for e in club_auth:
                    if ele['id'] in e:
                        # print(ele['id'])
                        sum_ += 1
    return sum_

# gets journal citation for a paper
def get_jour_cit(auth, all_data_papers, pap_id):
    return len(list(all_data_papers[str(pap_id)]['ref_auth'].values())[0])

# calculates the parameters for different paper values [dataframe] returns a json
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
        all_data_papers[str(paper_id)] = {'centrality value': paper_values[paper_id] , 'coauthors': coauth}
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
            club_cit[a] = get_club_cit_paper(club[a], cit_auth[a])
            jour_cit[a] = get_jour_cit(a, all_data_papers, paper_id)
        all_data_papers[str(paper_id)].update({'club_citation': club_cit, 'journal_citations': jour_cit})


        
    data_json = json.dumps(all_data_papers)
    # print(data_json)
    return(data_json)


'''values to be calculated for'''
'''if author ids in a list, use calculate()'''
''' change  file paths'''


# values = [179778838,92438100,1963576484,2148425697,	2467740887,	2150527135,] # author ids with degree 20
# values = [134769616,563069026,2619985137,2100767082,2038901907] # degree 10
# calculate(values)


### uncomment and run direct each output to a json file, so uncomment and run 2 lines at a time

# deg_coauth = pd.read_csv(path+'degreenodes_graph/degree_coauth.csv')
# ei_coauth =  pd.read_csv(path+'degreenodes_graph/eigen_coauth.csv')
# btw_coauth =  pd.read_csv(path+'degreenodes_graph/between_coauth.csv')

# unccomment the above lines

# sort_deg_coauth = deg_coauth.sort_values(by=['x'], ascending = False).head(5)
# calculate_all(sort_deg_coauth)

# sort_ei_coauth = ei_coauth.sort_values(by=['vector'], ascending = False).head(5)
# calculate_all(sort_ei_coauth)

# sort_btw_coauth = btw_coauth.sort_values(by=['x'], ascending = False).head(5)
# calculate_all(sort_btw_coauth)






### uncomment and run direct each output to a json file, so uncomment and run 2 lines at a time

# ei_cit =  pd.read_csv(path+'degreenodes_graph/eigen_cit.csv').sort_values(by=['vector'], ascending = False)
# btw_cit =  pd.read_csv(path+'degreenodes_graph/between_cit.csv').sort_values(by=['x'], ascending = False)
deg_cit = pd.read_csv(path+'degreenodes_graph/degree_cit.csv').sort_values(by=['x'], ascending = False)

# unccomment the above lines
final_deg_dict = pre_processing_for_cit(deg_cit)
value = calculate_all_papers(final_deg_dict)
print(value)

# final_ei_dict = pre_processing_for_cit(ei_cit)
# value = calculate_all_papers(final_ei_dict)
# print(value)

# final_btw_dict = pre_processing_for_cit(btw_cit)
# value = calculate_all_papers(final_btw_dict)
# print(value)
