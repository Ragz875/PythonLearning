a=[-1,-3,-5]
max=a[0]
for i in range(1,len(a)):
    if max < a[i]:
        max=a[i]
print(max)
