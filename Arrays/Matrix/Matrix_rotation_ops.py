def display(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end=' ')
        print()

def transpose(m):
    print('Transposed Matrix:')
    for i in range(len(m)):
        for j in range(i,len(m)):
            m[j][i],m[i][j] = m[i][j], m[j][i]
    display(m)
    return m

def reverse(m):
    for ele in m:
        ele.reverse()
    return(m)

def rotate_90(a):
    at=transpose(a)
    atr=reverse(at)
    print('after 90 deg clock rotate')
    display(atr)

def rotate_90_anti(a):
    ar=reverse(a)
    print('after reverse')
    display(ar)
    art = transpose(ar)
    print('after 90 deg Anti clock rotate')
    display(art)


a=[[1,2],[3,4]]
#a=[[1,2,3],[4,5,6],[7,8,9]]
print('Origina matrix : ')
display(a)
rotate_90(a)
#a=[[1,2,3],[4,5,6],[7,8,9]]
print('Origina matrix : ')
#display(a)
#rotate_90_anti(a)

"""
Rotate +90 : Transpose + Reverse 
Rotate -90 : Reverse + Transpose  
Rotate +180: Rotate +90 twice 
Rotate -180: Rotate -90 twice
"""