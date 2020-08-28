# graphml_samira
Graph ML programs

This repository contains, four python code files. The Embedding.py will save the model and nodeemb files on your machine for future use.

To run the programs you need to install Node2vec (I used this repository https://github.com/eliorc/node2vec). Also some python libraries such as Pandas, numpy and Networkx is needed.

Then you can launch the progrms with running the codes "criminal atm+towers.py" to get a list of atm and towers invonved in the criminal event. To find the criminal withdrawals you need to launch the "finding criminal withdrawals.py". If you need to slice the data in the "slicing.py" you just input the dataset file neme which containes the tower--phone, withdrawals, atm--phones list all in a file with three columns, with the header  "Source", "Target" and "time".
