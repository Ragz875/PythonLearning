# dups if element is repeated max 2 times and each ele in array range 1 < n
# conditions we are not suppose to use any addtional data structures
def dups(arr):
    for ele in arr:
        if arr[abs(ele)-1] > 0:
            arr[abs(ele)-1]= -arr[abs(ele)-1]
        else:
            print(abs(ele))

# if array element is repeated max 2 times and f array element can be of any size then use %,
# use below code for all the times
def dupsmod(arr):
    n=len(arr)
    for ele in arr:
        if arr[(abs(ele)-1)%n] > 0:
            arr[(abs(ele)-1)%n]= -arr[(abs(ele)-1)%n]
        else:
            print(abs(ele))

if __name__ == '__main__':
    print('main has started')

    a=[4,10, 10,4]
    dupsmod(a)