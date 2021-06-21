def matrixdiagonal(mat):
    if len(mat)==0:
        return []
    m,n= len(mat),len(mat[0])
    row,col=0,0
    #initiyze the array with zeors
    res=[0 for i in range(m*n)]
    for i in range(m*n):
        #print(mat[row][col])
        res[i]=mat[row][col]
        # deciding row col while traversing upside
        if (row+col)%2 == 0:
            if col==n-1:
                row = row + 1
            elif row == 0:
                col = col + 1
            else:
                row = row-1
                col = col+1
        # deciding row col while traversing downside
        else:
            if row == m-1:
                col = col + 1
            elif col == 0:
                row = row+1
            else:
                row=row + 1
                col=col - 1
    print('Result is:',res)

m=[[1,2,3],[4,5,6],[7,8,9]]
matrixdiagonal(m)



