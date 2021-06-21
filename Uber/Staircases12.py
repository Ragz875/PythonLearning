"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
solution is n th fibonacci number but start with 1,2 instead 0,1
"""
n=5
fib=[1,2]
i=2
while i <=n:
    fib.append(fib[i-1] + fib[i-2])
    i=i+1
print(fib)
print(fib[n-1])

