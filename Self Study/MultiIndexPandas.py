import numpy as np
import pandas as pd
import os

#df = pd.read_csv("Test.csv", header=[0, 1], encoding="utf8")
df = pd.DataFrame(abs(np.random.randn(10, 4)))

df.columns = [['ต้นทุนต่อหน่วย', 'ต้นทุนต่อหน่วย', 'ราคาขายต่อหน่วย', 'ราคาขายต่อหน่วย'], ['ทางตรง', 'ทางอ้อม', 'ทางตรง', 'ทางอ้อม']]
df.columns.names = [' ', ' ']

#df.index([" " for i in range(len(df))])

Column = [i for i in df]
BigLine   = "\n***************************************************************************" 
SmallLine = "\n\t-----------------------"

print(SmallLine,"\n\t แสดง DataFrame ทั้งหมด",SmallLine)
print("\n\n {}".format(df))
print(BigLine)

print(SmallLine,"\n\t แสดง Data of ต้นทุนต่อหน่วย",SmallLine)
print("\n\n {}".format(df['ต้นทุนต่อหน่วย']))
print(BigLine)

print(SmallLine,"\n\t แสดง Data of ต้นทุนทางอ้อมต่อหน่วย",SmallLine)
print("\n\n {}".format(df['ต้นทุนต่อหน่วย']['ทางอ้อม']))
print(BigLine)

print(SmallLine,"\n\t แสดง Data of ต้นทุนและราคาขาย ทางตรงต่อหน่วย",SmallLine)
print("\n\n {}".format(df[[('ต้นทุนต่อหน่วย', 'ทางตรง'), ('ราคาขายต่อหน่วย', 'ทางตรง')]]))
print(BigLine)

print(SmallLine,"\n\t แสดง Data of ต้นทุนทางอ้อมต่อหน่วย record 3",SmallLine)
print("\n\n {}".format(df['ต้นทุนต่อหน่วย']['ทางอ้อม'][2]))
print(BigLine)

print(SmallLine,"\n\t แสดง the first 3 records of ต้นทุนทางอ้อมต่อหน่วย data",SmallLine)
print("\n\n {}".format(df['ต้นทุนต่อหน่วย']['ทางอ้อม'][:3]))
print(BigLine)

print(SmallLine,"\n\t แสดง Data of ต้นทุนและราคาขาย ทางตรงต่อหน่วย record 3",SmallLine)
print("\n\n {}".format(df[[('ต้นทุนต่อหน่วย', 'ทางตรง'), ('ราคาขายต่อหน่วย', 'ทางตรง')]].iloc[2:3]))
print(BigLine)

print(SmallLine,"\n\t แสดง the first 3 records of ต้นทุนและราคาขาย ทางตรงต่อหน่วย",SmallLine)
print("\n\n {}".format(df[[('ต้นทุนต่อหน่วย', 'ทางตรง'), ('ราคาขายต่อหน่วย', 'ทางตรง')]].iloc[:3]))
print(BigLine)

print(SmallLine,"\n\t เอา the first 3 records of ต้นทุนและราคาขาย ทางตรงต่อหน่วย มาแปลงเป็น array",SmallLine)
print("\n\n {}".format(np.array(df[[('ต้นทุนต่อหน่วย', 'ทางตรง'), ('ราคาขายต่อหน่วย', 'ทางตรง')]].iloc[:3])))
print(BigLine)



df.to_csv("Test.csv", encoding='utf-8-sig', index=False)
df.to_excel("Test.xlsx", sheet_name="Sheet1")
