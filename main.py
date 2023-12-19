import requests
import pandas as pd
from datetime import datetime
import os



def FileCheck(name:str):
    if os.path.isfile(name):
        os.remove(name)

def GetOpenData (fileName:str): 
    domain_Url = 'https://data.gov.tw/api/front/dataset/export?format=csv'
    rep = requests.get(domain_Url)
    FileCheck(fileName)
    open(f"/Users/zhung/py/meeting/{fileName}","wb").write(rep.content)

def NewCSV(fileName:str):
    dt = pd.read_csv(fileName)
    df = pd.DataFrame(dt)
    d = df[["資料集名稱","主要欄位說明","資料下載網址"]]
    FileCheck("new.csv")
    d.to_csv("new.csv")

def AnalyzeCSV():
    print("Input your key word")
    keyWord = input()
    print(f"search keyword : {keyWord}....")
    dt = pd.read_csv("new.csv")
    q = dt[dt.資料集名稱.str.contains(keyWord)]
    print(q.values)

def Main():
    time = datetime.now()
    fileName = f"DataSet/OpenDataSet_{time.year}_{time.month}_{time.day}.csv"

    GetOpenData(fileName)
    NewCSV(fileName)
    # AnalyzeCSV()


Main()