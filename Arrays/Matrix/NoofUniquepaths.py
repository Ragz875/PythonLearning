# No of Unique path in a grid from (0,0) to (n*n)
# conditions : you can only travel down or right
def paths(n,m):
    if n==1 or m==1:
        return 1
    return paths(n,m-1) + paths(n-1,m)

print(paths(10,10))



