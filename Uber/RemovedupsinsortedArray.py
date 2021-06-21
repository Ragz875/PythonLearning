a=[1,1,2,2,3,4]
i=0
while i < len(a)-1:
    if a[i] == a[i+1]:
        del a[i]
    else:
        i=i+1
print(a)