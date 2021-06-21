def binadd(ab,bb):
    a,b=int(ab,2),int(bb,2)
    while b:
        ans=a^b
        print(f'ans: {ans}')
        carry= (a&b) << 1
        print(f'carry: {carry}')
        a,b=ans,carry
    print(bin(a)[2:])

def binadd_1(ab,bb):
    a, b = int(ab, 2), int(bb, 2)
    print(bin(a+b)[2:])

def bintodec(a):
    n=len(a)-1
    i=0
    ans=0
    while n >= 0:
        if a[n]=='1':
            ans+= 1 * (2 ** i)
        else:
            ans+= 0 * (2 ** i)
        n=n-1
        i=i+1
    return ans

def dectobin(a):
    if a > 1:
        dectobin(a//2)
    a=[]
    a.append(a%2)
    print(a)


#binadd_1('101','1')
#print(bintodec('1010'))
dectobin(10)