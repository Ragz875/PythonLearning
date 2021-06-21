# Use Dynamic Programming
def fib(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    print(f)
    return f[n]

#missing number
if __name__ == '__main__':
    nums=[0,1,2,4]
    missing=len(nums)
    for i,ele in enumerate(nums):
        print(missing,' ^= ',i, ' ^ ', ele)
        missing ^= i ^ ele

    print(f'missing element {missing}')

    nums=[7,6,4,3,1]
    min_price=nums[0]
    max_profit=0

    for i in range(1,len(nums)):
        if nums[i] < min_price:
            min_price=nums[i]
        elif nums[i]-min_price > max_profit:
            max_profit= nums[i]-min_price
    print('max_profit is :',max_profit)

    print('factorial of number is:')
    fact=1
    n = 10
    while n >=1 :
        fact = fact * n
        n=n-1
    print('Fact : ', fact)

# space optimization over Dynamic program example
    print('Fibonacci')
    a=0
    b=1
    n=9
    print(a,b,end='\n')
    for num in range(2,n+1):
        c=a+b
        print(c)
        (a,b)=(b,c)

    print(fib(9))


