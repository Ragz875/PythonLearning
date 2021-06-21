a=[[0,4],[1,3]]
b=[[3,2],[5,1]]

#a+b = [[3,6],[6,4]]

for i in range(len(a)):
    for j in range(len(b)):
        print((a[i][j] + b[i][j]), end=' ')
    print('')
