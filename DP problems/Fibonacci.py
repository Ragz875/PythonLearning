# Fiboacci starts with 0 1 (1 2 3)
# range Fibonacci Iterative O(n)
def fibiterative(low,high):
    a=0
    b=1
    i=1
    while i <= high:
        if b >=low :
            print(i,b)
        a,b=b,(a+b)
        i=i+1

# Better approach bottom up dynemic programing no extra storage just O(n)
def fib(n):
    a=0
    b=1
    i=1
    while i <=n:
        print(f'{i}:{b}')
        a,b=b,a+b
        i=i+1

# recursive memorization time : O(n) cache space: O(n)
# without memorization just recursion need o(n) stack space, time O(2 ** n) because two feb calls
def fibrecurrsive(n,cache):
    if n in cache:  return cache[n]
    if n <= 2:  return 1

    cache[n] = fibrecurrsive(n-1,cache) + fibrecurrsive(n-2,cache)
    return cache[n]

# Tabulization technique

def tabFib(n):
    print('tabulization started')
    fib= [0] * (n+1)
    fib[1]=1
    print(fib)
    i=0
    while i < len(fib)-1:
        fib[i+1]+=fib[i]
        fib[i+2]+=fib[i]
        i=i+1

    print(fib)
    return fib[n]



if __name__=='__main__':
    #fibiterative(1,6)
    #print('Recursive with memorization started')
    #cache={}
    #print(fibrecurrsive(50,cache))
    #print(cache)
    #fib(50)
    print(tabFib(6))