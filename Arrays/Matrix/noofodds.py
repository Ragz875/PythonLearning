class matrix:
    def __init__(self,n,m):
        print('Constructor invoked')
        self.n,self.m = n,m
        self.arr = [[0 for i in range(m)] for j in range(n)]

    def printarr(self):
        print(self.arr)

    def arrincrement(self,row,col):
        print('arrincrement started')
        for i in range(self.m):
            self.arr[row][i] += 1
        self.printarr()
        for j in range(self.n):
            self.arr[j][col] += 1

        self.printarr()
    def noofodds(self):
        print('no of odds called',self.arr, self.n, self.m)
        self.count=0
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] % 2 != 0:
                    self.count+=1
        return self.count

if __name__=='__main__' :
    ind=[[0,1],[1,1]]
    rows,cols = 3,2
    m=matrix(rows,cols)
    m.printarr()
    for row,col in ind:
        m.arrincrement(row,col)
    print('Number of odds in array:', m.noofodds())
