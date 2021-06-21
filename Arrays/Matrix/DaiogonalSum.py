class Dsum:
    def __init__(self):
        print('DSum constructor is called')
    # code for left diagnonal sum
    def sum(self,m):
        sum=0
        for i in range(len(m)):
            for j in range(len(m)):
                if i==j:
                    sum+=m[i][j]
        print('right dig sum:',sum)
        #sum1=0
    # code for right Diagonal sum
        for i in range(len(m)):
            for j in range(len(m)):
                if i+j == len(m)-1 and i!=j:
                    sum+= m[i][j]
                    print(f'm[{i}][{j}]')
        print('left + right daig sum :', sum)
    def simplediagsum(self,m):
        print(m, len(m))
        for i in range(len(m)):
            print(f'm[{i}][{len(m)}-1-{i}]')

        a= [m[i][len(m)-1-i] for i in range(len(m))] \
        #- ( len(m)%2 * m[len(m)//2][len(m)//2])
        # m[i][i] - primary Diagonal , m[i][len(m)-i-1] - secondary daigonal
        # make it zero for even dimensions , - center value for odd dimension len(m)%2 * m[len(m)//2][len(m)//2]
if __name__ == '__main__':
    print('main started')
    m=[[1,2,3],[4,5,6],[7,8,9]]
    #m=[[1,1,1],[1,1,1],[1,1,1]]

    o=Dsum()
    o.sum(m)
    #print('Simle Sum:', o.simplediagsum(m))
    #simplediagsum(m)


