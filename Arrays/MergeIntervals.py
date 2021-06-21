a=[[1,4],[4,5]]
merged=[]

a=[[1,5] , [12, 15],     [42, 44],
  [70, 72] ,   [36, 36],     [-4,  2],
  [43, 69]  ,  [15, 24]]

a.sort()
print(a)
for interval in a:
    if not merged or merged[-1][1] < interval[0] :
        merged.append(interval)
        print(merged)
    else:
        merged[-1][1]=max(merged[-1][1],interval[1])

print(merged)
