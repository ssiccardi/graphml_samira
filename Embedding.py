#! /usr/bin/env python3


import networkx as nx
from node2vec import Node2Vec
import csv
import numpy as np

EMBEDDING_FILENAME = 'nodeemb'
EMBEDDING_MODEL_FILENAME = 'model'

# Create a graph
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


# Precompute probabilities and generate walks - **ON WINDOWS ONLY WORKS WITH workers=1**
node2vec = Node2Vec(graph, dimensions=60, walk_length=40, num_walks=10, workers=4)  # Use temp_folder for big graphs

# Embed nodes
model = node2vec.fit(window=5
, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)

# Save embeddings for later use
model.wv.save_word2vec_format(EMBEDDING_FILENAME)

# Save model for later use
model.save(EMBEDDING_MODEL_FILENAME)

