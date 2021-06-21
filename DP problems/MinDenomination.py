# minimum number of coins needed to make target t
#DP using memorization technique to prevent the sample sub problem being solve again and agin
# Formula
# f(i,t) = min( f(i,t-val)+1 , f[i-1,t])
# final answer f(n-1,t)
#
import math
def changeMake(arr,target):
    cache={}
    def subproblem(i,t):
        print(cache)
        # check if this sub problem input is already solved - Memorization
        if (i,t) in cache:  return cache[(i,t)]

        # compute the lowest number of coins we need if choosing to take a coin of the current denomination
        val= arr[i]
# case 1 : Considering the val
        # current denomination is too large
        if val > t:
            choice_take = math.inf  #math infinity
        elif val==t:
            #target reached
            choice_take=1
        else:
            #take and recurse
            choice_take= 1 + subproblem(i,t-val)

# case 2 : compute the lowest number of coins we need if not taking any more coins of the current denomination
        if i==0:
            #not an option if no more denominations
            choice_leave = math.inf
            print(choice_leave)
        else:
            # recurse with remaining denominations
            choice_leave=subproblem(i-1,t)
        #in recursive these are the last steps
        #print(f'choice_take:{choice_take},choice_leave :{choice_leave}')
        optimum = min(choice_take,choice_leave)
        cache[(i,t)]=optimum
        return optimum
    return subproblem(len(arr)-1,target)

if __name__== '__main__':
    arr= [8,3,1,2]
    target=3

    print('main called:', changeMake(arr,target))
