#! /usr/bin/env python3

import tempfile
import gensim.models
import numpy as np
import csv

model = gensim.models.KeyedVectors.load_word2vec_format('nodeemb', binary=False)
from gensim.similarities.index import AnnoyIndexer
criminal_atm1 = []


# 100 trees are being used in this example
annoy_index = AnnoyIndexer(model, 100)

# Derive the vector for the word "science" in our model
vector1 = model.wv["a602"]


approximate_neighbors_atm1 = model.wv.most_similar('a602', topn = 1000)



for neighbor1 in approximate_neighbors_atm1:
    #print (neighbor[0])
    criminal_atm1.append(neighbor1[0])


tot_criminal = np.array(criminal_atm1)

criminal = []
criminal = criminal_atm1

result1 = [i for i in tot_criminal if i.startswith('a')]
result2 = [i for i in tot_criminal if i.startswith('t')]
result3 = [i for i in tot_criminal if i.startswith('p')]


criminal_vec = []
criminal_vec_keys = []

for i in result1:
    criminal_vec.append(model.wv.most_similar(i, topn = 30))

    
for j in range(len(criminal_vec)):
    for k in range(len(criminal_vec[j])):
         criminal_vec_keys.append(criminal_vec[j][k][0])

plus_criminal = np.array(criminal_vec_keys)

 
towers = [i for i in plus_criminal if i.startswith('t')]
unique_towers = np.unique(np.concatenate((towers,result2)))

counting_towers = {}
similarity_towers = {}

for item in unique_towers:
    if item in result2:
        counting_towers[item] = 1
    else:
        counting_towers[item] = 1
        
 
for i in towers:
    counting_towers[i] += 1



for item in result2:
    for i in range(len(approximate_neighbors_atm1)):
        if approximate_neighbors_atm1[i][0] == item :
            similarity_towers[item] = approximate_neighbors_atm1[i][1]
            
for iitem in list(np.unique(towers)):
    for i in range(len(criminal_vec)):
        if criminal_vec[i][0] == iitem :
            similarity_towers[iitem] = criminal_vec[i][1]
    


a = counting_towers.values()
b = max(a)

if b == 1:
    criminal_tower = []
else:
    
    criminal_tower = [max(similarity_towers, key=similarity_towers.get)]
    
from numpy import savetxt



np.savetxt('criminal_atms.csv', result1, delimiter=',', fmt = '%s')
np.savetxt('criminal_towers.csv', criminal_tower, delimiter=',', fmt = '%s')

####dimension reduction + plotting
from sklearn.decomposition import IncrementalPCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np                                  # array handling




def reduce_dimensions(model):
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    vectors = [] # positions in vector space
    labels = [] # keep track of words to label our data again later
    for word in model.wv.vocab:
        vectors.append(model.wv[word])
        labels.append(word)

    # convert both lists into numpy vectors for reduction
    vectors = np.asarray(vectors)
    labels = np.asarray(labels)

    # reduce using t-SNE
    vectors = np.asarray(vectors)
    tsne = TSNE(n_components=num_dimensions, random_state=0, perplexity= 30)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels




x_vals, y_vals, labels = reduce_dimensions(model)
def plot_with_matplotlib(x_vals, y_vals, labels):
    import matplotlib.pyplot as plt
    import random

    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)
    #plt.show()

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    for i in indices:
        #print (str(labels[i]))
        if labels[i] in criminal and labels[i] in result1:
           plt.annotate(labels[i], (x_vals[i], y_vals[i]), color = 'red')
        #if labels[i] in result1 and labels[i] not in criminal_atm:
        #  plt.annotate(labels[i], (x_vals[i], y_vals[i]), color = 'blue')
        if labels[i] in criminal and labels[i] in result2:
           plt.annotate(labels[i], (x_vals[i], y_vals[i]), color = 'orange')
        if labels[i] in criminal and labels[i]  in result3:
           plt.annotate(labels[i], (x_vals[i], y_vals[i]), color = 'green')
          
    plt.show()

plot_with_matplotlib(x_vals, y_vals, labels)

