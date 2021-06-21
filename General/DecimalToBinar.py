def dectoBin(num):
    if num > 1:
        dectoBin(num//2)
    print(num%2,end='')

dectoBin(15)

