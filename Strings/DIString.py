class DIstring:
    def diStringMatch(self,str):
        largest = len(str)
        smallest = 0
        list= []
        print('initial list:', list)

        for char in str:
            if char == 'I':
                list.append(smallest)
                smallest += 1
            elif char == 'D':
                list.append(largest)
                largest -= 1
        # we need to add this to satisfy If S[i] == "I", then A[i] < A[i+1] ,
        # if S[i] == "D", then A[i] > A[i+1]
        print('smallest:',[smallest] )
        return list + [smallest]

if __name__ == '__main__' :
    strarray=['IDID','III','DDI','IID','DDD']

    obj = DIstring()
    for str in strarray:
        print(str, ':', obj.diStringMatch(str))







