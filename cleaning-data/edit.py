import pandas as pd
df = pd.read_excel(io="kalka (mine data ).xlsx")
li = []
for i in df["Ps Address"]:
	stri = i.split(",")
	li.append(stri[-1])
fi = open("new.csv","w")
stri = "AC,PS Name,Ps Address"
fi.write(stri)
for i,j,k in zip(df["AC"],df["PS Name"],range(len(df["AC"]))):
	stri = "\n"+str(i)+","+str(j)+","+str(li[k])
	fi.write(stri)
