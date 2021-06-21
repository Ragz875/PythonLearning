#Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move to either index i or
# index i + 1 on the next row.
# Could you do this using only O(n) extra space, where n is the total number of rows in
# the triangle?

# this one is correct
def minimumTotalDP(triangle):
    base = [0] * (len(triangle) + 1)
    print(base)
    for i in range(len(triangle)-1, -1, -1 ):
        base=[min(base[b], base[b+1])+ triangle[i][b] for b in range(i+1)]
        print(base)
    return base

arrs=[[2],[3,4],[6,5,7],[4,1,8,-3]]
minimumTotalDP(arrs)
