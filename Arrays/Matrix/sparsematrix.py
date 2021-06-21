# formual total zeros count > (row * col)//2
def sparsematrix(a):
    zero_count=0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                zero_count+=1
    if zero_count > (len(a)*len(a[0]))//2:
        return True
    else:
        return False

array = [ [ 1, 1, 0 ],
          [ 0, 0, 4 ],
          [ 6, 0, 0 ] ]

if (sparsematrix(array)) :
    print("Yes")
else :
    print("No")

