# since it is sorted matrix so bin search is optimal
class countNeg:
    def convstrcount(self,mat):
        return str(mat).count('-')

    def negcount(self,mat):
        cnt=0
        for row in mat:
            left = self.binsearch(row)
            #print('row:',row,'left:',left )
            cnt += len(row) - left
        return cnt

    def binsearch(self,row):
       lower=0
       upper=len(row)-1
       print('initial lower :', lower ,'initial upper :', upper)
       while lower <= upper:
           mid = (lower + upper) // 2
           print('Mid :', mid,'row[mid] :', row[mid])
           if row[mid] < 0:
               upper = mid - 1
               print('upper :', upper)
           else:
               lower = mid + 1
               print('lower :', lower)
       return lower


if __name__ == '__main__' :
    print('Main has started')
    mat=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    #mat=[[1,-1],[-1,-1]]
    mat=[[4, 3, 2, -1]]
    obj=countNeg()
    print('convstrcount: ',obj.convstrcount(mat))
    print('negcount: ',obj.negcount(mat))



