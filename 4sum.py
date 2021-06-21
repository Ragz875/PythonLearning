def sum4():
    m={}
    cnt=0
    for a in A:
        for b in B:
          m[a+b] = m.get(a+b,0) + 1
    for c in C:
        for d in D:
            cnt+= m.get(-(c+d),0)
    print("no of tuples :",cnt)

if __name__=='__main__' :
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
sum4()

