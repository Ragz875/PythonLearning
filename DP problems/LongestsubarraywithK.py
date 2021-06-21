def longest_min_sum(A,k):
    # dictionary mydict implemented
    # as hash map
    mydict = dict()
    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0
    # traverse the given array
    for i in range(len(A)):
        # accumulate the sum
        sum += A[i]
        # when subArray starts from index '0'
        if (sum == k):
            maxLen = i + 1
            print(maxLen)

        # check if 'sum-k' is present in
        # mydict or not
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])

        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i
    print(mydict)
    print(f'sum: {sum}, i:{i}, sum - k : {sum - k},mydict[sum - k], {sum - k}')
    return maxLen


# Driver Code
if __name__ == '__main__':
    A=[0, 0, 1, 1, 1, -1, 2, 3, 2]
    n = len(A)
    k = 3
    print("Length =", longest_min_sum(A, n, k))