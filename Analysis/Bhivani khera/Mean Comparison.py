import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(io="bhiwani khera final2014.xlsx",sheet_name="Sheet1")
parties = ['INLD', 'BJP', 'HJCBL', 'INC','SMBHP', 'RBC', 'SP', 'HALP', 'RPP(LB)', 'IND', 'IND2', 'IND3', 'IND4','IND5', 'IND6', 'IND7', 'IND8', 'IND9', 'IND10', 'IND11', 'IND12']
votes = []
top_parties = []
t_parties = []
low_parties = []
l_parties = []
top_votes = []
low_votes = []
t_parties_per = []
l_parties_per = []
top_parties_per = []
low_parties_per = []
com = []
nescom = []
colors1=[]
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
for i in range(len(nescom)):
    for j in range(len(nescom[i])):
        if nescom[i][j] > mean[i]:
            t_parties.append(df.iloc[j,1])
            t_parties_per.append(nescom[i][j])
        else:
            l_parties.append(df.iloc[j,1])
            l_parties_per.append(nescom[i][j])
    if t_parties != []:
        top_parties.append(t_parties)
        top_parties_per.append(t_parties_per)
        t_parties=[]
        t_parties_per=[]
    if l_parties != []:
        low_parties.append(l_parties)
        low_parties_per.append(l_parties_per)
        l_parties=[]
        l_parties_per=[]
#print(low_parties_per)
for k in range(0,6):
    for i in range(len(top_parties[k])):
        colors1.append("green")
    for i in range(len(low_parties[k])):
        colors1.append("red")
    new_list_per=top_parties_per[k] + low_parties_per[k]
    new_list= top_parties[k]+low_parties[k]
    plt.pie(new_list_per,colors=colors1,labels=new_list,shadow=True,rotatelabels=True)
    #plt.pie(low_parties_per[0],colors=colors2,labels=low_parties[0],radius=0.5)
    plt.axis("equal")
    stri = "Task-6" + parties[k]
    plt.title(parties[k])
    plt.savefig(stri)
    plt.show()















