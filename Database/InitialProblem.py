import pandas as pd
import math

def monthlen(month, leap=0):
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap == 1 and month >= 2:    
        return sum(mon[:month]) + 1
    return sum(mon[:month])

def lenday(date1, date2):
    yr1 = int(date1[:4])
    yr2 = int(date2[:4])
    m1  = int(date1[4:6])
    m2  = int(date2[4:6])
    d1  = int(date1[6:])
    d2  = int(date2[6:])
    if yr1 == 2020 and yr2 == 2021:
        return (monthlen(m2-1) + d2 + monthlen(12, leap=1)) - (monthlen(m1-1, leap=1) + d1)
    else:
        return (monthlen(m2-1) + d2) - (monthlen(m1-1) + d1)

Hos  = pd.read_excel("MockData.xlsx", sheet_name="A")
Pat  = pd.read_excel("MockData.xlsx", sheet_name="B")
Serv = pd.read_excel("MockData.xlsx", sheet_name="C")
Msup = pd.read_excel("MockData.xlsx", sheet_name="D")

pat = Pat.merge(Serv, on="Pid")
Q1 = pd.DataFrame()
L = ["Pid", "repdate", "Hcode", "dateadm"]
for i in L:
    Q1[i] = pat[i]
nday = []
for i in range(len(pat)):
    date2 = str(int(pat["dateadm"][i]))
    date1 = str(int(pat["repdate"][i]))
    nday.append(lenday(date1, date2))
Q1["wait"] = nday
Q1.to_excel("Q1.xlsx", index=False)

Q2 = pd.DataFrame()
pat = pat.merge(Hos, on="Hcode")
L = ["Pid", "ppostcode", "hpostcode"]
for i in L:
    Q2[i] = pat[i]
Q2.to_excel("Q2.xlsx", index=False)

Q3 = pd.DataFrame()
pat = Pat.merge(Msup, on="Pid")
pat = pat.merge(Serv, on="Pid")
L = ["Pid", "Hcode_x", "omask", "omdateb", "omdatee", "ohighflow", "ohdateb", "ohdatee", "vent", "vdateb", "vdatee", "ecmo", "edateb", "edatee", "dateadm", "datedsc"]
for i in L:
    Q3[i] = pat[i]
LOS = []
for i in range(len(pat)):
    date1 = str(int(pat["dateadm"][i]))
    date2 = str(int(pat["datedsc"][i]))
    LOS.append(lenday(date1, date2))
Q3["LOS"] = LOS

OMlen = []
for i in range(len(pat)):
    if pat["omask"][i] == 1 and not (math.isnan(pat["omdateb"][i]) or math.isnan(pat["omdatee"][i])):
        date1 = str(int(pat["omdateb"][i]))
        date2 = str(int(pat["omdatee"][i]))
        OMlen.append(lenday(date1, date2))
    else:
        OMlen.append(0)
Q3["OMlen"] = OMlen

OHlen = []
for i in range(len(pat)):
    if pat["ohighflow"][i] == 1 and not (math.isnan(pat["ohdateb"][i]) or math.isnan(pat["ohdatee"][i])):
        date1 = str(int(pat["ohdateb"][i]))
        date2 = str(int(pat["ohdatee"][i]))
        OHlen.append(lenday(date1, date2))
    else:
        OHlen.append(0)
Q3["OHlen"] = OHlen

Ventlen = []
for i in range(len(pat)):
    if pat["vent"][i] == 1 and not (math.isnan(pat["vdateb"][i]) or math.isnan(pat["vdatee"][i])):
        date1 = str(int(pat["vdateb"][i]))
        date2 = str(int(pat["vdatee"][i]))
        Ventlen.append(lenday(date1, date2))
    else:
        Ventlen.append(0)
Q3["Ventlen"] = Ventlen

ECMOlen = []
for i in range(len(pat)):
    if pat["ecmo"][i] == 1 and not (math.isnan(pat["edateb"][i]) or math.isnan(pat["edatee"][i])):
        date1 = str(int(pat["edateb"][i]))
        date2 = str(int(pat["edatee"][i]))
        ECMOlen.append(lenday(date1, date2))
    else:
        ECMOlen.append(0)
Q3["ECMOlen"] = ECMOlen


Q3.to_excel("Q3.xlsx", index=False)
