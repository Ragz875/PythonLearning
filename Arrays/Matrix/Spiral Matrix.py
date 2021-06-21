a= [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]
a= [ [1,2,3],[4,5,6], [7,8,9]]
res=[]
#Initial positions in matrix
left, right = 0, len(a[0])
top, bottom,= 0, len(a)

while (left < right and top < bottom):
    # get every i in top row
    for i in range(left, right):
        res.append(a[top][i])
    top = top + 1
    # get every i in right colum
    for i in range(top, bottom):
        res.append(a[i][right-1])
    right=right-1

    print(f'{left} < {right} and {bottom} < {top}')
    if not (left < right and top < bottom):
        break

    # get every i in the bottom row
    for i in range(right-1, left-1, -1):
        res.append(a[bottom-1][i])
    bottom = bottom - 1

    # get every i in left column
    for i in range(bottom-1,top-1,-1):
        res.append(a[i][left])
    left = left + 1

print('Clock spiral:',res)
res.reverse()
print('anti Clock spiral:',res)

