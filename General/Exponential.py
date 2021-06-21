# e^x = 1 + x/1! + x^2/2! + x^3/3! + ......
# e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) )

def exponential(n,x):
    sum=1.0
    for i in range(n,0,-1):
        print(f'{sum} = 1 + {x} * {sum}//{i} --> ')
        sum = 1 + x * sum/i

    print(sum)


n=10
x=1
exponential(n,x)
