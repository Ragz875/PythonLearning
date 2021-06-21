def printprime(low, high):
    print(f'low: {low} high:{high}')
    for num in range(low,high):
        #print(num)
        if all( num%n!=0 for n in range(2,num)) and num!=1:
            print(num)

printprime(1,20)