import requests
import pandas
from datetime import datetime
import os

def GetOpenData ():
    domain_Url = 'https://data.gov.tw/api/front/dataset/export?format=csv'
    rep = requests.get(domain_Url)
    time = datetime.now()
    fileName = f"{time.year}_{time.month}_{time.day}.csv"
    if os.path.isfile(f"DataSet/{fileName}"):
        os.remove(f"DataSet/{fileName}")
    open(f"/Users/zhung/py/meeting/DataSet/{fileName}","wb").write(rep.content)

def AnalyzeCSV():
    time = datetime.now()
    fileName = f"{time.year}_{time.month}_{time.day}.csv"
    df = pandas.read_csv(f"DataSet/{fileName}") 
    print(df.columns)
    print(df["資料集名稱"].value_counts)
       

def Main():
    GetOpenData()
    AnalyzeCSV()


Main()