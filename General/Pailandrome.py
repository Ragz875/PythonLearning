def arrpail(a):
    pail=True
    for i in range(len(a)//2):
        if a[i]!=a[-(i+1)]:
            print('not pailandrome')
            pail=False
            break
    if pail:
        print('Array is pailandrome :')

def strpail(s):
    pail=True
    for ind in range(len(s)//2):
        if s[ind] != s[-(ind+1)]:
            pail=False
            break
    if pail:
        print('Given string is pailendrome')
    else:
        print('Given string is not a pailendrome')

def numrangepail(n):
    print('range pail is called:',n)
    for i in range(n):
        if numpail(i):
            print(i)

def numpail(j):
    rev=0
    i=j
    print(' original value:', j)
    while i > 0:
        rev=rev * 10 + i%10
        i//=10
    print(' rev value:', rev)
    return (j == rev)



if __name__=='__main__':
    print('Main started')
    a = [1, 2, 3, 5, 3, 2, 1]
    arrpail(a)
    s='abbab'
    strpail(s)
    numrangepail(25)


