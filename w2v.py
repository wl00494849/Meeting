from gensim.models.word2vec import KeyedVectors
from gensim.models import Word2Vec

def Main():
    model = KeyedVectors.load_word2vec_format("/Users/zhung/py/meeting/tmunlp_1.6B_WB_300dim_2020v1.bin.gz",
                                                            unicode_errors='ignore', 
                                                            binary=True)
    model = Word2Vec()
    
    print(model["人口"])
    print(len(model["人口"]))
    ## Cosine similarity Value 1 to -1 heighest value more similarity
    print("人口、人數")
    print(model.similarity("人口","人數"))

    print("人口相似詞")
    for w, sim in model.most_similar('人口', topn=5):
        print((w,sim))
    
    print("地址相似詞")
    for w, sim in model.most_similar('地址',topn=3):
        print((w,sim))
    
Main()