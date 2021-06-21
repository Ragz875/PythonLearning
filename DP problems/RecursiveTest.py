# 1 recursive call tree with one node at each level  - total elements n
# 2 recursive calls tree with two nodes at each level - total elements 2^n -1
# 3 recursive calls tree with three nodes at each level - total elements 3^n -1
def recurtest(n):

    if n < 1:   return 1
    recurtest(n-1)
    recurtest(n-1)
    recurtest(n - 1)
    print(n)


if __name__== '__main__':
    recurtest(3)
