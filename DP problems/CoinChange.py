# DP with memorization technique
def coinChange(targetSum,arr,arrlen,cache={}):
    if targetSum ==0:   return 1
    if targetSum < 0:   return 0
    if arrlen == 0:    return 0
    #if targetSum in cache:  return cache[targetSum]
    #print('test')

    return coinChange(targetSum-arr[0],arr,arrlen) + coinChange(targetSum,arr[1:],arrlen-1)
    #return cache[targetSum]

# the fewest number of coins that you need to make up that amount.
def coinChangemincount(amount,coins):
    table = [amount + 1] * (amount + 1)
    # trivial value 0 total with 0 coin
    table[0] = 0

    for i in range(1, len(table)):
        for coin in coins:
            if i - coin >= 0:
                table[i] = min(table[i], 1 + table[i - coin])

    # while retruning ensure no default value is considered
    if table[amount] != amount + 1:
        return table[amount]
    else:
        return -1


#print('test')
print('minmum coins needed to make target 11,[1,2,5]:',coinChangemincount(11,[1,2,5]))
print('minmum coins needed to make target 3,[8,3,1,2]:',coinChangemincount(3,[8,3,1,2]))
print('Tot number of ways to make target 11,[1,2,5] :', coinChange(11,[1,2,5],3))
print('Tot number of ways to make target  3,[8,3,1,2] :', coinChange(3,[8,3,1,2],4))

#print(coinDenom(3,[8,3,1,2]))