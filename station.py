import pandas as pd
from openpyxl.workbook import Workbook 
df = pd.read_excel(io="Ambala Cantt.xlsx",sheet_name="2009")
strm=[]
for i in df["Station"]:
    stri=i.split(',')
    strm.append(stri[-1])
df1 = pd.DataFrame(strm)
print(df1)
writer = pd.ExcelWriter("Ambala Cantt.xlsx")
df1.to_excel(writer,sheet_name="2009")
writer.save()
