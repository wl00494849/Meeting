import requests
import pandas
from datetime import datetime

def GetOpenData ():
    domain_Url = 'https://data.gov.tw/api/front/dataset/export?format=csv'
    rep = requests.get(domain_Url)
    time = datetime.now()
    fileName = f"{time.year}_{time.month}_{time.day}"
    open(f"/Users/zhung/py/meeting/DataSet/{fileName}.csv","wb").write(rep.content)
    
def main():
    GetOpenData()

main()