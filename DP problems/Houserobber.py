def rob(nums):
    r1, r2 = 0, 0
    for amount in nums:
        temp= max(amount+r1, r2)
        r1, r2 = r2,temp
    print('Max amount of rob:', r2)
# formula max(val + f(n-2) or f(n-1))
def MaxFlowerPlant(arr):
    a=0 #f(n-2)
    b=0 #f(n-1)

    for val in arr:
        temp=max(val+a,b)
        a,b= b,temp
    print('max sum of non-consecutive elements:',b)

if __name__ =='__main__':
    a=[3,10,3,1,2,5]
    MaxFlowerPlant(a)
    rob(a)






