"""
hints:
    M               N
row , col       row  , col
i      k                j
i,k * k,j
"""

def MatrixMultiplication(M,N,mrow_len, mcol_len, nrow_len, ncol_len):
    R=[[0 for col in range(ncol_len)] for row in range(mrow_len)]
    for i in range(mrow_len):
        for j in range(ncol_len):
            for k in range(mcol_len):
                R[i][j]+= M[i][k] * N[k][j]
    display(R)

def display(res):
    for i in range(mrow_len):
        for j in range(ncol_len):
            print(res[i][j],end=' ')
        print()


M = [[1, 1, 1],     [2, 2, 2],     [3, 3, 3],     [4, 4, 4]]
N = [[1, 1, 1, 1],     [2, 2, 2, 2],     [3, 3, 3, 3] ]
M = [[1, 2], [3, 4]]
N = [[4, 5], [6, 7]]
#M = [[1, 1, 1, 1],    [2, 2, 2, 2],    [3, 3, 3, 3],    [4, 4, 4, 4]]
#N = [[1, 1, 1, 1],    [2, 2, 2, 2],    [3, 3, 3, 3],    [4, 4, 4, 4]]

mrow_len=len(M)
mcol_len=len(M[0])

nrow_len=len(N)
ncol_len=len(N[0])

if mcol_len==nrow_len:
    print(f'Given Matrices {mrow_len}x{mcol_len} * {nrow_len}X{ncol_len} result is = {mrow_len}X{ncol_len} ')
    MatrixMultiplication(M,N,mrow_len, mcol_len, nrow_len, ncol_len)
else:
    print(f'Given Matrices length {mrow_len}x{mcol_len} * {nrow_len}X{ncol_len} ')
    print('Matix multiplication is not allowed')
