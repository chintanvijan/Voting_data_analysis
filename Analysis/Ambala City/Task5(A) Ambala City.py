import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
df1 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2014")
df2 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2009")
df3 = pd.read_excel(io="Ambala City.xlsx",sheet_name="2005")
t1=0
t2=0
t3=0

s1=[]
s2=[]
s3=[]
p1=[]
p2=[]
p3=[]
p4 = [42.84,2.27,34.11,0,0,0,0,0,0]
p5 = [38.18,7.78,33.27,0,0,0,0,0,0]

l1 = ['BJP', 'BSP', 'INC', 'HaLP', 'SAD', 'HJCPV','HJC(BL)','RLD','INLD']
l2 = ['BJP', 'BSP', 'INC', 'HaLP', 'SAD','HJCPV','HJC(BL)', 'RLD','INLD']
l3 = ['BJP', 'BSP', 'INC', 'HaLP', 'SAD', 'HJCPV','HJC(BL)','RLD','INLD']

for i in range(len(df1.Station)):
    t1 = t1+ df1.Total[i]
for i in range(len(df2.Station)):
    t2 = t2+ df2.Total[i]
for i in range(len(df3.Station)):
    t3 = t3+ df3.Total[i]

for i in range(len(l1)):
    if i>4 :
        s1.append(0)
    else:
        s1.append(df1[l1[i]].sum())
for i in range(len(l2)):
    if i==3 or i==5 or i==8:
        s2.append(0)
    else: 
        s2.append(df2[l2[i]].sum())
for i in range(len(l3)):
    if i>2 and i<8:
        s3.append(0)
    else:
        s3.append(df3[l3[i]].sum())
for i in range(len(s1)):
    p1.append((s1[i]/t1)*100)
for i in range(len(s2)):
    p2.append((s2[i]/t2)*100)
for i in range(len(s3)):
    p3.append((s3[i]/t3)*100)

x = ["2014","2009","2005","2000","1996"] 
for i in range(len(p1)):
    plt.bar(x[0],p1[i],label=p1[i])
    plt.bar(x[1],p2[i],label=p2[i])
    plt.bar(x[2],p3[i],label=p3[i])
    plt.bar(x[3],p4[i],label=p4[i])
    plt.bar(x[4],p5[i],label=p5[i])
    plt.xlabel("Year")
    plt.ylabel("Parties")
    plt.grid()
    plt.title(l1[i])
    plt.legend()
    stri = "Task5(A)" + l1[i]
    #plt.show()
    plt.savefig(stri)
    plt.gcf().clear()


















