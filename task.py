import json


def beb(d):
    for j in range(len(d)):
        if isinstance(d[j], list):#1. Из массива удаляются все элементы с четным индексом.
        
            s = " ".join([str(d[j][i]) for i in range(len(d[0])) if i % 2 ==1])    
            
            d[j]=s 
        elif isinstance(d[j], dict):#2. Все ключи словаря переводятся в верхний регистр.
            q = dict((k.upper(), v) for k, v in d[j].items()) 
            d[j] = q
        elif isinstance(d[j], str):
            p = str(d[j])
            l = int(len(p)/2)
            y = p[0:l]
            d[j] = y
    print(d)
    return d


with open("test.json", "r+") as f:
    t = json.load(f)
    print(len(t[0]))
    d = t
    beb(d)
    t = d
    f.seek(0)
    f.write(json.dumps(t, indent =4))
    f.close()
    
