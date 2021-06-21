n=9
tm=0
while n > 1:
    tm += n//2
    n = n//2 + n % 2

print('Total number of matches :',tm)


