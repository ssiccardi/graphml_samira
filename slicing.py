import csv
import pandas as pd


df = pd.read_csv ('dataset.csv')


i = 0
idx2 = 0

while len(df)- idx2 > 1:

    
    a = df['time'][0]+(i*7200)      #slicing by 2h
    b = df['time'][0]+((i+1)*7200)

    if b > df["time"].iloc[-1]:
        b = df["time"].iloc[-1]



    df['Time' + str(i)] = df['time'].loc[(df['time'] >= a) &
                                             (df['time'] <= b)]

    idx = pd.Index(df['Time' + str(i)].dropna())

    idx1 = df[df['time'] == idx[0]].index.values.astype(int)[0]
    idx2 = df[df['time'] == idx[-1]].index.values.astype(int)[0]
    df['Source' + str(i)] = df['Source'][idx1:idx2+1]
    df['Target' + str(i)] = df['Target'][idx1:idx2+1]
    

    df['Source' + str(i)] = df['Source' + str(i)].dropna()
    df['Target' + str(i)] = df['Target' + str(i)].dropna()

    file_name = "time" + str(i) +".csv"
    df.to_csv(file_name, sep = ',', columns = ['Source' + str(i), 'Target' + str(i)], index = False)
    i = i + 1
