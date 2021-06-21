# core logic to return the partition index for recursive division
def partition(start,end,ele):
    pivot_ind=start
    pivot_val=ele[pivot_ind]
    start = pivot_ind + 1
    end=len(ele) - 1

    print('before while :',start, ' ', end )
    while start < end :
        print('start')
        while ele[start] <= pivot_val and start < len(ele):
            print('ele[start] :', ele[start], ' start : ', start, 'len(ele) :', len(ele))
            start += 1
        while ele[end] > pivot_val:
            end -= 1
        # swap
        if start < end:
            (ele[start],ele[end]) =(ele[end], ele[start])

    (ele[pivot_ind],ele[end]) = (ele[end],ele[pivot_ind])

    return end

# driving method
def quicksort(start,end,ele):
# returns partition index
    if start < end :
        pi= partition(start,end,ele)
        quicksort(start,pi-1,ele) # left partition
        quicksort(pi+1, end, ele) # right partition


if __name__ == '__main__' :
    print('I am in main method')
    ele = [5,4,3,2,1]
    print('Orginal array : ', ele)
    start=0
    end=len(ele)-1
    quicksort(start,end,ele)
    print(ele)

"""
    test_cases=[[],
                [5,4,3,2,1],
                [1,2,3,4,5],
                [2,1]]
    i=0
    for each_case in test_cases:
        quicksort(0, len(each_case)-1,each_case)
        print(each_case)
        i=i+1

    print(test_cases)
"""

