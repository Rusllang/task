import json

#1. Из массива удаляются все элементы с четным индексом.
#2. Все ключи словаря переводятся в верхний регистр.
#3. Из каждой строки удаляется вторая половина символов.
#4. Остальные элементы остаются без изменений.

def beb(d):
    for j in range(len(d)):
        if isinstance(d[j], list):
        
            s = ' '.join([str(d[j][i]) for i in range(len(d[0])) if i % 2 ==1])    
            print(s)
            d[j]=s
        elif isinstance(d[j], dict):
            print(d[j])


with open("test.json", "r+") as f:
    t = json.load(f)
    print(len(t[0]))
    #list s = []
    d = t
    beb(d)
    
