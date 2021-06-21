# time complexity sqrt of x
def sqrt(x):
    # x range is from 0 to n
    if x < 2:
        return x
    i=1
    while i <= x//2:
        if i*i == x:
            return i
        if i*i > x:
            return i-1
        i=i+1
# better complexity log n
def sqrt1(x):
    if x==0 or x == 1:
        return x
    low=0
    high= x//2
    i=1
    while low <= high:
        mid= (low + high) // 2
        if mid * mid == x :
            return mid
        elif mid * mid < x:
            low = mid + 1
            ans=mid
        else:
            high=mid - 1
        i+=1
    print('Total calls :',i)
    return ans


for num in range(4,10,1):
    print(f'sqaureroot of {num} is : ', sqrt(num))

