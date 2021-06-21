""" Given by siri
Given an array of positive integers nums and a positive integer target, return the minimal length
of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
or equal to target. If there is no such subarray, return 0 instead.Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
# not working
nums = [2,3,1,2,4,3]
#nums=[1,4,4]
target=7
max_so_far=0
temp=[]
j=0
arr_len_so_far=0
max_arr_len=len(nums)
i=0
while i < len(nums):
    if max_so_far < target:
        max_so_far += nums[i]
        temp.append(nums[i])
        i = i + 1
        if i == len(nums) and j!=0:
            i=j+1
        #if i==len(nums) and j==0:
        #    print('0')
        #    break
        print(temp, 'max so far:', max_so_far,len(temp), i, j)
    else:
        arr_len_so_far=len(temp)
        print(arr_len_so_far,max_arr_len)
        if arr_len_so_far < max_arr_len:
            max_arr_len=arr_len_so_far
            #print('max_arr_len:',arr_len_so_far)
        j=j+1
        i=j
        temp=[]
        max_so_far=0
print(temp)
print(i)







