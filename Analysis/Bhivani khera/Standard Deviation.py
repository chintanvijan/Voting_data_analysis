import pandas as pd
import matplotlib.pyplot as plt
import math
df1 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2014")
df2 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2009")
df3 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2005")
df4 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2014")
df5 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2009")
df6 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2005")
df7 = pd.read_excel(io="Mulana(SC).xlsx",sheet_name="2014")
df8 = pd.read_excel(io="Mulana(SC).xlsx",sheet_name="2009")
df9 = pd.read_excel(io="Mulana(SC).xlsx",sheet_name="2005")
parties1 = ['BJP', 'BSP', 'INC', 'INLD', 'NJC', 'HLP', 'HJCP','IND', 'IND.1', 'IND.2', 'IND.3', 'IND.4']
parties2 = ['BJP', 'NCP', 'INC', 'BSP', 'INLD','HJCP', 'IND', 'IND.1', 'IND.2', 'IND.3', 'IND.4']
parties3 = ['INC', 'BSP', 'BJP', 'NCP', 'NLP','IND', 'IND.1']
parties4 = ['BJP', 'BSP', 'INC', 'HaLP', 'SAD', 'HJCPV', 'IND','IND.1', 'IND.2', 'IND.3', 'IND.4', 'IND.5', 'IND.6', 'NOTA']
parties5 = ['HJC(BL)', 'BSP', 'INC', 'BJP', 'RLD', 'SAD', 'IND','IND.1', 'IND.2']
parties6 = ['INC', 'BJP', 'INLD', 'BSP', 'IND','IND.1', 'IND.2', 'IND.3']
parties7 = ['BSP', 'HJC(BL)', 'INLD', 'INC', 'BJP', 'HLP','IND', 'IND.1', 'Unnamed: 10', 'Unnamed: 11', 'NOTA']
parties8 = ['HJC(BL)', 'BSP', 'INC', 'BJP', 'INLD', 'NCP', 'BRP','SRP', 'IND', 'IND.1']
parties9 = ['BJP', 'BSP', 'INC', 'INLD', 'ES', 'LD','IND', 'IND.1']
p = []
def func(df,parties):
    votes = []
    com = []
    nescom = []
    sd = []
    for i in range(len(parties)):
        votes.append(df[parties[i]].sum())
    #print(votes)
    for i in range(len(parties)):
        for j in range(len(votes)):
            if votes[i] > votes[j]:
                t = votes[i]
                m = parties[i]
                votes[i]=votes[j]
                parties[i] = parties[j]
                votes[j]=t
                parties[j]=m
    p.append(parties)
    #print(votes)
    #print(parties)
    mean = []
    t_rows = len(df.axes[0])
    for i in range(0,6):
        x = df[parties[i]].sum()
        y= t_rows
        z=x/y
        mean.append(z)
    #print(y)
    #print(mean)
    for j in range(0,6):
        for index,row in df.iterrows():
            com.append(row[parties[j]])
        #print(com)
        nescom.append(com)
        com = []
    #print(nescom)
    s=0
    l=0
    standev=0
    for i in range(len(nescom)):
        temp=0
        for j in range(len(nescom[i])):
            temp=temp+((nescom[i][j]-mean[i])*(nescom[i][j]-mean[i]))
        #   print(temp)
        s = math.sqrt(temp)
        l=(len(nescom[i])) - 1
        #print(l)
        standev = s/l
        sd.append(standev)
    #print(sd)
    return sd
l1 = func(df1,parties1)
print(l1)
l2 = func(df2,parties2)
print(l2)
l3 = func(df3,parties3)
print(l3)
l4 = func(df4,parties4)
print(l4)
l5 = func(df5,parties5)
print(l5)
l6 = func(df6,parties6)
print(l6)
l7 = func(df7,parties7)
print(l7)
l8 = func(df8,parties8)
print(l8)
l9 = func(df9,parties9)
print(l9)
print(p)















