# write a function which takes target sum and the array. The function should return a boolean whether or not
# it is possible to generate the target sum using numbers from the array
# conditions: you may use the element of array as many times as needed you may assume that array elements
# are non-ve numbers, # brute Force time O(n ^ m) , space O(n)
# Dynemic mem technique time - O(n*m), space - O(n)
# n - array length , m is target sum (represents height)

# Can Sum is Decision Problem
def canSum(targetsum,arr,cache):
    if targetsum==0:    return True
    if targetsum < 0:   return False
    if targetsum in cache:  return cache[targetsum]

    for num in arr:
        rem = targetsum - num
        if canSum(rem,arr,cache):
            cache[targetsum]=True
            #print(cache)
            return True

    cache[targetsum] = False
    print(cache)
    return False
# Tabulation technique - Visualize the problem as a table
def canSumtab(targetSum,nums):
    # size the table based on inputs, #initilize the table with default values
    table = ['False'] * (targetSum+1)
    # seed the trivial answer into the table,
    # means 0 possible with 0 numbers
    table[0]=True
    for i in range(len(table)):
        if table[i]== True:
            for num in nums:
                if i+num <= targetSum:  table[i+num]= True
    print(table)
    return table[targetSum]



#canSumtab(7,[2,3]) #True
print(canSumtab(7,[2,3])) # True
#print(canSumtab(7,[5,3,4,7])) # True
#print(canSumtab(7,[2,4])) # False
#print(canSumtab(300,[7,14])) # False