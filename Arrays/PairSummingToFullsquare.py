def sqrt(num):
    print('passed number',num)
    if num==1 or num==0:
        return True
    if num < 0:
        return False
    i=1
    res=1
    while res <=num:
        i = i+1
        res = i*i
        if res==num:
            #print(f'num : {num}, i: {i}')
            return True


a=[-1,2,3,0,6]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(f'{a[i]} + {a[j]} =', a[i]+a[j])
        if sqrt(int(a[i])+int(a[j])):
            count=count+1
print(f'number of pairsummingtofullsqaure:', count)


