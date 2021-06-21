# write a code to find number ways you can traverse from start(0,0) to bottom(n*m) in a Grid
# conditions traverse either right or down only# time and space complexity
# Brute Force - O(2 ^ (n+m)) , space - O(n+m)
# Memorization: O(n*m)=o(n), space O(n+m)=o(n) , below is memorization technique
def GridTraverse(row,col,cache):
    if row==0 or col==0:    return 0
    if (row,col)==(1,1): return 1
    if (row,col) in cache:    return cache[(row,col)]

    cache[(row,col)]= GridTraverse(row-1,col,cache) + GridTraverse(row,col-1,cache)
    #final return
    return cache[(row,col)]

cache={}
print(GridTraverse(18,18,cache))
print(cache)