# bestsum should retrun an array containing the shortest combination of numbers that add up to
# exactly the targetsum . If there is a tie for the shortest combination then return any of
# the shortest
# Brute force without cache Time: O(m^n * m), space O(m)
# with cache Time: O(m* n * m), space O(m*m)

# best sum is an optimization problem
def bestSum(targetsum,arr,cache={}):
    if targetsum < 0: return None
    if targetsum ==0: return []
    if targetsum in cache: return cache[targetsum]

    shortest=None

    for num in arr:
        #print('started :', num)
        rem=targetsum-num
        remcomb=bestSum(rem,arr,cache)
        if remcomb != None:
            temp=remcomb+[num]
            print('temp:', temp,'shortest :',shortest)
            if shortest is None or len(temp) < len(shortest):
                shortest=temp
    cache[targetsum] = shortest
    return shortest

# Tabulation technique - Visualize the problem as a table
# tips if null then replace, if not then compare lengths of array time O(m * n * m), space : o(m*m)
def bestSumTab(targetsum,arr):

    table= [None] * (targetsum+1)
    table[0]=[]

    for i in range(len(table)):
        if table[i] != None:
            for num in arr:
                combination = table[i] + [num]
                if ( i+num < len(table)) and (not table[i+num] or len(table[i+num]) > len(combination)):
                    table[i+num] = combination
    print(table)
    return table[targetsum]



print(bestSumTab(7,[5,3,4,7])) # [5,3]
#print(bestSum(10,[1,2,5,25])) # [5,3]
#print(bestSum(7,[5,3,4,7]))
