import pandas as pd
import matplotlib.pyplot as plt
import math
df1 = pd.read_excel(io="bhiwani khera final2014.xlsx",sheet_name="Sheet1")
parties1 = ['INLD', 'BJP', 'HJCBL', 'INC','SMBHP', 'RBC', 'SP', 'HALP', 'RPP(LB)', 'IND', 'IND2', 'IND3', 'IND4','IND5', 'IND6', 'IND7', 'IND8', 'IND9', 'IND10', 'IND11', 'IND12']
df2 = pd.read_excel(io="bawani_khera2009final.xlsx",sheet_name="Sheet1")
parties2 = ['INLD', 'BSP', 'BJP','HJC(BL\n)', 'INC', 'USP', 'SBP', 'HSP', 'IND', 'IND2', 'IND3', 'IND4','IND5', 'IND6', 'IND7', 'IND8', 'IND9', 'IND10', 'IND11']
p = []
total = []
def func(df,parties,count_var):
    votes = []
    nescom_per = []
    com = []
    nescom = []
    sd = []
    per = []
    comper=[]
    countper=[]
    comcountper=[]
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
    #print(df["Total"])
    for i in range(len(nescom)):
        for j in range(len(nescom[i])):
            t = (nescom[i][j]/df.Total[j])*100
            per.append(t)
        comper.append(per)
        per = []
    #print(comper)
    for i in range(len(nescom)):
        for j in range(0,5):
            countper.append(0)
        comcountper.append(countper)
        countper=[]
    #print(comcountper)
    for i in range(len(comper)):
        for j in range(len(comper[i])):
            if comper[i][j] <= 10:
                comcountper[i][0] = comcountper[i][0] + 1
            elif comper[i][j] >10 and comper[i][j]<=20:
                comcountper[i][1] = comcountper[i][1] + 1
            elif comper[i][j] >20 and comper[i][j]<=30:
                comcountper[i][2] = comcountper[i][2] + 1
            elif comper[i][j]>30 and comper[i][j]<=40:
                comcountper[i][3] = comcountper[i][3] + 1
            else:
                comcountper[i][4] = comcountper[i][3] + 1
    print(comcountper)
    val = [">10%","10-20%","20-30%","30-40","40+"]
    for j in range(len(comcountper)):
        for i in range(0,5):
            plt.bar(val[i],comcountper[j][i])
        plt.xlabel("Vote Percentage")
        plt.ylabel("No. of booths")
        plt.title(parties[j])
        if count_var == "2009" and j==2:
            stri = "Task 6 (" + count_var +") HJC(BL)"
        else:
            stri = "Task 6 (" + count_var +")" + parties[j]
        plt.savefig(stri)
        plt.show()
func(df1,parties1,"2014")
func(df2,parties2,"2009")














