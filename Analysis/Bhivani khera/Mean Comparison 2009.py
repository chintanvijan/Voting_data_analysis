import pandas as pd
import matplotlib.pyplot as plt
#df = pd.read_excel(io="bawani_khera2009final.xlsx",sheet_name="Sheet1")
#parties = ['INLD', 'BSP', 'BJP','HJC(BL\n)', 'INC', 'USP', 'SBP', 'HSP', 'IND', 'IND2', 'IND3', 'IND4','IND5', 'IND6', 'IND7', 'IND8', 'IND9', 'IND10', 'IND11']
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
def func(df,parties,year_str):
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
    #print(df.columns)
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
        #if k==2:
        #   stri = "Task-6 HJC(BL)"
        #else:
        stri = "Task-6" + parties[k]
        plt.title(parties[k])
        plt.savefig(stri)
        plt.show()

func(df1,parties1,"Ambala Cantt(2014)")
func(df2,parties2,"Ambala Cantt(2009)")
func(df3,parties3,"Ambala Cantt(2005)")
func(df4,parties4,"Ambala City(2014)")
func(df5,parties5,"Ambala City(2009)")
func(df6,parties6,"Ambala City(2005)")
func(df7,parties7,"Mulana(SC)(2014)")
func(df8,parties8,"Mulana(SC)(2009)")
func(df9,parties9,"Mulana(SC)(2005)")













