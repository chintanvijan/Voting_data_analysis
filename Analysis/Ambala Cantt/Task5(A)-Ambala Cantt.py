import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
df1 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2014")
df2 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2009")
df3 = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2005")
t1=0
t2=0
t3=0
t1bjp=0
t1bsp=0
t1inc=0
t1inld=0
t1njc=0
t1hlp=0
t1hjcp=0
t1pbjp=0
t1pbsp=0
t1pinc=0
t1pinld=0
t1pnjc=0
t1phlp=0
t1phjcp=0

t2bjp=0
t2ncp=0
t2inc=0
t2bsp=0
t2inld=0
t2hjcp=0
t2pbjp=0
t2pncp=0
t2pinc=0
t2pbsp=0
t2pinld=0
t2phjcp=0

t3inc=0
t3bsp=0
t3bjp=0
t3ncp=0
t3nlp=0
t3pinc=0
t3pbsp=0
t3pbjp=0
t3pncp=0
t3pnlp=0

for i in range(len(df1.Station)):
    t1 = t1+ df1.Total[i]
for i in range(len(df2.Station)):
    t2 = t2+ df2.Total[i]
for i in range(len(df3.Station)):
    t3 = t3+ df3.Total[i]

for i in range(len(df1.Station)):
    t1bjp = t1bjp+ df1.BJP[i]
for i in range(len(df1.Station)):
    t1bsp = t1bsp+ df1.BSP[i]
for i in range(len(df1.Station)):
    t1inc = t1inc+ df1.INC[i]
for i in range(len(df1.Station)):
    t1inld = t1inld+ df1.INLD[i]
for i in range(len(df1.Station)):
    t1njc = t1njc+ df1.NJC[i]
for i in range(len(df1.Station)):
    t1hlp = t1hlp+ df1.HLP[i]
for i in range(len(df1.Station)):
    t1hjcp = t1hjcp+ df1.HJCP[i]

for i in range(len(df2.Station)):
    t2bjp = t2bjp+ df2.BJP[i]
for i in range(len(df2.Station)):
    t2ncp = t2ncp+ df2.NCP[i]
for i in range(len(df2.Station)):
    t2inc = t2inc+ df2.INC[i]
for i in range(len(df2.Station)):
    t2bsp = t2bsp+ df2.BSP[i]
for i in range(len(df2.Station)):
    t2inld = t2inld+ df2.INLD[i]
for i in range(len(df2.Station)):
    t2hjcp = t2hjcp+ df2.HJCP[i]

for i in range(len(df3.Station)):
    t3inc = t3inc+ df3.INC[i]
for i in range(len(df3.Station)):
    t3bsp = t3bsp+ df3.BSP[i]
for i in range(len(df3.Station)):
    t3bjp = t3bjp+ df3.BJP[i]
for i in range(len(df3.Station)):
    t3ncp = t3ncp+ df3.NCP[i]
for i in range(len(df3.Station)):
    t3nlp = t3nlp+ df3.NLP[i]


t1pbjp = (t1bjp/t1)*100
t1pbsp = (t1bsp/t1)*100
t1pinc = (t1inc/t1)*100
t1pinld = (t1inld/t1)*100
t1pnjc = (t1njc/t1)*100
t1phlp = (t1hlp/t1)*100
t1phjcp = (t1hjcp/t1)*100
t1pncp=0
t1pnlp=0

t2pbjp = (t2bjp/t2)*100
t2pncp = (t2ncp/t2)*100
t2pinc = (t2inc/t2)*100
t2pbsp = (t2bsp/t2)*100
t2pinld = (t2inld/t2)*100
t2phjcp = (t2hjcp/t2)*100
t2pnjc=0
t2phlp=0
t2pnlp=0

t3pinc = (t3inc/t3)*100
t3pbsp = (t3bsp/t3)*100
t3pbjp = (t3bjp/t3)*100
t3pncp = (t3ncp/t3)*100
t3pnlp = (t3nlp/t3)*100
t3pinld=0
t3phjcp=0
t3phlp=0
t3pnjc=0

l1 = [t1pbjp,t2pncp,t1pinc,t1pbsp,t1pinld,t1phjcp,t1pnjc,t1phlp,t1pnlp]
l2 = [t2pbjp,t2pncp,t2pinc,t2pbsp,t2pinld,t2phjcp,t2pnjc,t2phlp,t2pnlp]
l3 = [t3pbjp,t3pncp,t3pinc,t3pbsp,t3pinld,t3phjcp,t3pnjc,t3phlp,t3pnlp]
l4 = [29.09 , 1.21 , 22.66 , 0.46 , 0 , 0,0 ,0,0,0 ]
l5 = [22.17 , 0 , 29.36,0.27,0,0,0,0,0]
l = ["bjp","ncp","inc","bsp","inld","hjcp","njc","hlp","nlp"]

x = ["2014","2009","2005","2000","1996"] 
for i in range(len(l1)):
    fig,ax=plt.subplots()
    plt.bar(x[0],l1[i],label=l1[i])
    plt.bar(x[1],l2[i],label=l2[i])
    plt.bar(x[2],l3[i],label=l3[i])
    plt.bar(x[3],l4[i],label=l4[i])
    plt.bar(x[4],l5[i],label=l5[i])
    plt.xlabel("Year")
    plt.ylabel("Parties")
    plt.grid()
    plt.title(l[i])
    plt.legend()
    stri = "Task5(A)" + l[i]
    #plt.show()
    plt.savefig(stri)
    plt.gcf().clear()

















