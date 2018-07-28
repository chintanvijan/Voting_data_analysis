import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2014")
dbjp ={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dbsp={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dinc={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dinld={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dnjc={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dhlp={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
dhjcp={'Mandor': '', 'Khatoli': '', 'Panjokhra': '', 'Kalarheri': '', 'Janetpur': '', 'Garnala': '', 'Barnala': '', 'Dhankor': '', 'Tundli': '', 'Tundla': '', 'Boh': '', 'Ramgarh': '', 'Babyal': '', 'Dalipgarh': '', 'Ambala Cantt.': '', 'Rampur Sarsheri': '', 'Sarsheri': '', 'Khojkipur': '', 'Kardhan': '', 'Nanhera': '', 'Brahaman Majra': '', 'Ghasitpur': '', 'Machhounda': '', 'Shahpur': '', 'Bara': ''}
li = []
for k in dbjp:
    dbjp[k]=0
for i in range(len(df.Station)):
    
        dbjp[df.Station[i]]=dbjp[df.Station[i]]+ df.BJP[i]

for k in dbsp:
    dbsp[k]=0
for i in range(len(df.Station)):
    
        dbsp[df.Station[i]]=dbsp[df.Station[i]]+ df.BSP[i]

for k in dinc:
    dinc[k]=0
for i in range(len(df.Station)):
    
        dinc[df.Station[i]]=dinc[df.Station[i]]+ df.INC[i]

for k in dinld:
    dinld[k]=0
for i in range(len(df.Station)):
    
        dinld[df.Station[i]]=dinld[df.Station[i]]+ df.INLD[i]

for k in dnjc:
    dnjc[k]=0
for i in range(len(df.Station)):
    
        dnjc[df.Station[i]]=dnjc[df.Station[i]]+ df.NJC[i]        

for k in dhlp:
    dhlp[k]=0
for i in range(len(df.Station)):
    
        dhlp[df.Station[i]]=dhlp[df.Station[i]]+ df.HLP[i]        

for k in dhjcp:
    dhjcp[k]=0
for i in range(len(df.Station)):
    
        dhjcp[df.Station[i]]=dhjcp[df.Station[i]]+ df.HJCP[i]

li.append(dbjp)
li.append(dbsp)
li.append(dinc)
li.append(dinld)
li.append(dnjc)
li.append(dhlp)
li.append(dhjcp)
#print(li)
mdf = pd.DataFrame(li)
print(mdf)
    
