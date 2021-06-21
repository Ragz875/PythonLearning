# similar to Cancel sum The function should return an array containing any combination of elements
# that add up to exactly the targetsum. If there is no combination that adds up to the targetsum then return null
# if there are multiple combination possible, you may return any single one
# time: O(n * m * m)
#space : O(m*m)

# howsum is combinatoric problem
def howSum(targetsum,arr,cache={}):
    if targetsum ==0:   return []
    if targetsum < 0:   return None
    if targetsum in cache:  return cache[targetsum]
    globala=[]
    for num in arr:
        rem = targetsum-num
        remresult=howSum(rem,arr,cache)
        if remresult != None:
            # extra m space because of append
            cache[targetsum]= remresult + [num]
            return cache[targetsum]

    cache[targetsum]=None
    return None

# Tabulation technique - Visualize the problem as a table, Note here you need to know only one combination output of all
# possibilities.
# time : o(m*n*m), space O(m * m)
def howsumtab(targetsum,arr):
    table= [None] * (targetsum+1)
    table[0]=[]
    #print(table)
    for i in range(len(table)):
        if table[i]!= None:
            for num in arr:
                if i+num < len(table):  table[i+num]=table[i]+ [num]
    #print(table)
    return table[targetsum]


print('7,[2,3]:', howsumtab(7,[2,3])) # [3,2,2]
print('7,[5,3,4,7]:', howsumtab(7,[5,3,4,7])) # [4,3]
print('7,[2,4]:', howsumtab(7,[2,4])) # null
print('8,[2,3,5]:', howsumtab(8,[2,3,5])) # [2,2,2,2]
print('300,[7,14]:', howsumtab(300,[7,14]))# null
print('3,[8,3,1,2] :', howsumtab(3,[8,3,1,2]))#
print('5,[1,2,5] :', howsumtab(5,[1,2,5]))#