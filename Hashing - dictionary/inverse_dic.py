dic={'a':1,'b':2,'c':3}
dic1={}
print(dic)
for key,val in dic.items():
    dic1[val]=key
dic.clear()
print(dic1)