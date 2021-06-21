""" You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock
Input: prices = [7,1,5,3,6,4]
Output: 5
"""
a=[7,1,5,3,6,4]

max_profit=0
min_so_far=a[0]
i=1
while i < len(a):
    if a[i] < min_so_far:
        min_so_far=a[i]
    elif a[i]-min_so_far > max_profit:
        max_profit=a[i]-min_so_far
    i=i+1

#print(max_profit)
print(min_so_far)


