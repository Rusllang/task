import json


#3. �� ������ ������ ��������� ������ �������� ��������.
#4. ��������� �������� �������� ��� ���������.

def beb(d):
    for j in range(len(d)):
        if isinstance(d[j], list):#1. �� ������� ��������� ��� �������� � ������ ��������.
        
            s = ' '.join([str(d[j][i]) for i in range(len(d[0])) if i % 2 ==1])    
            print(s)
            d[j]=s
        elif isinstance(d[j], dict):#2. ��� ����� ������� ����������� � ������� �������.
            print("bebra")

            print(d[j].keys())
            for i in d[j]:
                print(d[j])
                i.upper()
                #i = q
                #print(q)
            print(d[j].fromkeys(0))
#        elif isinstance(d[j], str):
    print(d)


with open("test.json", "r+") as f:
    t = json.load(f)
    print(len(t[0]))
    #list s = []
    d = t
    beb(d)
    
