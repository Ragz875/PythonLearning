# Binary Search Iteration
def BinsearchIterative(a, val):
    lower = 0
    upper = len(a) - 1

    while lower <= upper :
        mid = (lower + upper) // 2
        if val == a[mid]:
            return mid
        elif val < a[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

# Binary search Recursion
def BinsearchRecurrsion(a, lower, upper, val):
    #base condition
    if lower > upper :
        return -1

    mid = (lower + upper) // 2
    if val == a[mid]:
        return mid
    elif val < a[mid]:
        return BinsearchRecurrsion(a,lower,mid - 1,val)
    else:
        return BinsearchRecurrsion(a, mid + 1, upper, val)


if __name__=='__main__':
    a=[1,2,3,4,5,10]
    print('Org array: ',a)
    print('Binary search using Iteration o/p')
    for val in a:
        print(f'value: {val} at index :', BinsearchIterative(a,val))

    print('Org array: ', a)
    print('Binary search using recursion o/p')
    lower=0
    upper=len(a)-1

    for val in a:
        print(f'value: {val} at index :', BinsearchRecurrsion(a,lower,upper,val))
