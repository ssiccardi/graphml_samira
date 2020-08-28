#! /usr/bin/env python3

import networkx as nx
import csv


graph = nx.Graph()

with open('time8.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    
    edges1 = [tuple(e1) for e1 in edgereader][1:]
    
    edges_list = []
    for e in edges1:

        edges_list.append(tuple(map(str, e)))

    edges3 = list(tuple(edges_list))
    
listtostr = ''.join(map(str, edges3))

graph = nx.Graph()
graph.add_edges_from(edges3)
atms_list = []

with open('criminal_atms.csv', 'r') as atmscsv:
    atmsreader = csv.reader(atmscsv)
    atms_list = [row for row in atmsreader]
    flat_list_atm = [item for sublist in atms_list for item in sublist]
    #print (flat_list_atm)
    neighbors_atms = [list(graph.neighbors(i)) for i in  flat_list_atm]


with open('criminal_towers.csv', 'r') as towerscsv:
    towersreader = csv.reader(towerscsv)
    towers_list = [row for row in towersreader]
    flat_list_towers = [item for sublist in  towers_list for item in sublist]
    neighbors_towers = [list(graph.neighbors(j)) for j in  flat_list_towers]

common = []
b = set(list(graph.neighbors('a602'))).intersection(set(list(graph.neighbors('t42513'))))

for j in range(len(flat_list_atm)):
    a = list(set(neighbors_towers[0]).intersection(set(neighbors_atms[j])))
    c = list(set(a)- set(b))
    common.append(a)


empty_index = []
res_common = [ele for ele in common if ele != []]

for i in range(len(common)):
    if common[i] == []:
        empty_index.append(flat_list_atm[i])


new_atm_list = [ele for ele in flat_list_atm if ele not in empty_index]



with open('list_of_criminal_withdrawals.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    
    for i, atm_id in enumerate(flat_list_atm):
           csvwriter.writerow([flat_list_atm[i], common[i]])
            
        






            
