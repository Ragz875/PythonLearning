#  multiple buy/sell allowed. Find the max profit on over all.
# hits - accumulate maxprofit only when prices[i] - prices[i - 1]

prices = [1,2,3,4,5]
maxprofit = 0
i=1
while i < len(prices):
    if (prices[i] > prices[i - 1]):
        maxprofit += prices[i] - prices[i - 1]
    i=i+1
print(maxprofit)