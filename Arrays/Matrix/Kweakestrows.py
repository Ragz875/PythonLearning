"""
Given a m * n matrix mat of ones (representing soldiers) and
zeros (representing civilians), return the indexes of the k weakest rows in the matrix
ordered from the weakest to the strongest.
"""
def kweakestrows(mat,k):
    weaks =  [ (sum(row), index) for index, row in enumerate(mat) ]
    print(weaks)
    weaks.sort()
    print(weaks)
    res=[]
    print(weaks)
    for i in range(k):
        res.append(weaks[i][1])
    print('index sort order :', res)

mat=[[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
mat= [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
k=2

kweakestrows(mat,k)



