import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import chi2
Hos  = pd.read_excel("MockData.xlsx", sheet_name="A")
Pat  = pd.read_excel("MockData.xlsx", sheet_name="B")
Serv = pd.read_excel("MockData.xlsx", sheet_name="C")
Msup = pd.read_excel("MockData.xlsx", sheet_name="D")
Q1   = pd.read_excel("Q1.xlsx")
Q34  = pd.read_excel("Q3&4.xlsx")


DeathIndex1, DeathIndex2, DeathIndex3, DeathIndex4, DeathIndex5  = [], [], [], [], []

Data            = pd.DataFrame()
Data["dscht"]   = Serv["dscht"]
Data["Pid"]     = Serv["Pid"]
Data["Hcode"]   = Serv["Hcode"]
Data["cohward"] = Serv["cohward"]
Data["aiir"]    = Serv["aiir"]
Data["maiir"]   = Serv["maiir"]
Death           = Data
Column          = ["DOB", "Gender", "totalbed", "drid", 
                   "drintensivist", "dranesth", "drtotal", "nursetotal",
                   "wait", "LOS", "OMlen", "OHlen", "Ventlen", "ECMOlen"]

Data1 = Data.merge(Hos, on="Hcode")
ColumnData = [i for i in Data1]
for i in Column:
    if i in ColumnData:
        Death[i] = Data1[i]

Data2 = Data.merge(Pat, on="Pid")
ColumnData = [i for i in Data2]
for i in Column:
    if i in ColumnData:
        Death[i] = Data2[i]

Data3 = Data.merge(Msup, on="Pid")
ColumnData = [i for i in Data3]
for i in Column:
    if i in ColumnData:
        Death[i] = Data3[i]

Data4 = Data.merge(Q1, on="Pid")
ColumnData = [i for i in Data4]
for i in Column:
    if i in ColumnData:
        Death[i] = Data4[i]

Data5 = Data.merge(Q34, on="Pid")
ColumnData = [i for i in Data5]
for i in Column:
    if i in ColumnData:
        Death[i] = Data5[i]

for i in range(len(Death)):
    Death["DOB"][i] = 2021 - int(str(Death["DOB"][i])[:-4])
    if Death["dscht"][i] == 9:
        Death["dscht"][i] = 1
    else:
        Death["dscht"][i] = 0
Death  = Death.fillna(0)
Y = (np.array(Death)[:,0]).astype("int")
X = np.array(Death)[:,3:] 

model = LogisticRegression()
model.fit(X, Y)
scores, pvalues = chi2(X, Y)

Q5 = pd.DataFrame()
Column = [i for i in Death][3:] + ["Intercept"]
Q5["Risk Factor"] = Column
Q5["Regression Coefficient"] = list(model.coef_[0]) + list(model.intercept_)
Q5["p-value"] = list(pvalues) + ["-"]

writer = pd.ExcelWriter('Q5.xlsx', engine='xlsxwriter')
Q5.to_excel(writer, index=False, sheet_name="Q5")
Death.to_excel(writer, index=False, sheet_name="Data")
writer.save()