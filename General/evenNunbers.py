def decide_even(start,n):
    print('called decide even')
    if start%2==0:
        printeven(start, n)
    else:
        print('else')
        printeven(start+1, n)

def printeven(start, count):
    new_end= start + 2* count
    while start < new_end:
        print(start, end=' ')
        start=start+2

decide_even(2,4)
decide_even(49,4)
decide_even(50,4)