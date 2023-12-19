import requests
import jieba


def GetData (): 
    domain_Url = 'https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big'
    rep = requests.get(domain_Url)
    open(f"/Users/zhung/py/meeting/Tradition_Chinese.txt.big","wb").write(rep.content)

def Main():
    jieba.set_dictionary("Tradition_Chinese.txt.big")
    text = "高雄市三民區"
    print('|'.join(jieba.cut(text)))

Main()