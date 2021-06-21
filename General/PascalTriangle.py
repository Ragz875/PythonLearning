def pascal(n):
    for line in range(1,n+1):
        c=1
        for i in range(1,line+1):
            print(c,end=' ')
            #if line==3 :
            #    print(f'({c}*({line}-{i}))//{i}')
            c= c*(line-i)//i
        print('')
        #n=n-1

def pascal1(n):
    len=n
    for i in range(n+1):
        sp=' ' * n
        print(sp,end='')
        for j in range(2*i+1):
            print('*',end='')
        print()
        n=n-1

def testpascal(numRows):
    list = []
    for line in range(1, numRows + 1):
        c = 1
        temp = []
        for i in range(1, line + 1):
            temp.append(c)
            #print(c,end='')
            c = c * (line - i) // i
        #print('')
        list.append(temp)
    print(list)

#pascal(5)
pascal1(3)