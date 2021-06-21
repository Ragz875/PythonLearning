# Maximum sub array can be contigious or non-contigious.Below code is for a contigious sub array when ever -ve/-ve  values
#are given encouter then it wont add it to the curr_sum as the expected answer would be -ve
# For non-contigiuos, its a maximum sum where you do not consider the -ve values
#Given an integer array nums, find the contiguous subarray (containing at least one
# number) which has the largest sum and return its sum. May contain -ve numbers
"""
-- hints -
# since it contains +ve and -ve so no chance that the target can be -ve
# no need to go back (apply window) , max_sum, sum_so_far will be adjusted as you go
#
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6."""

# this problem does not display any indices
def maxSubArray(nums):
    i = 0
    sum_so_far = 0
    max_sum = nums[0]
    while i < len(nums):
        # since it contains +ve and -ve so no chance that the target can be -ve
  #      print(max_sum)
        if sum_so_far < 0:
            sum_so_far = nums[i]
        else:
            sum_so_far += nums[i]
        if max_sum < sum_so_far:
            max_sum = sum_so_far
        i = i + 1
    return max_sum

# below solution captures the start and end values for contigious subarray, and subsequence arr
def maxSubArray1(nums):
    curr_sum=0
    curr_start = 0
    max_sum=nums[0]
    best_start=best_end=0
    sub_seq_sum=0
    for curr_end,val in enumerate(nums):
        # below code for sub array contigious
        if curr_sum < 0 :
            curr_start  = curr_end
            curr_sum=val
        else:
            curr_sum=curr_sum+val
        if curr_sum >
            :
            max_sum=curr_sum
            best_start=curr_start
            best_end=curr_end+1   # the +1 is to make 'best_end' exclusive

    #print(f'curr_start:, {curr_start}, curr_end: {curr_end}, best_start: {best_start}, best_end: {best_end}')
    print(nums[best_start:best_end])
    # below code for sub array non-contigious.
    # sort to ensure if complete array is -ve values
    nums.sort()
    sub_seq_sum=nums[-1]
    if sub_seq_sum >=0:
        sub_seq_sum=0
        for val in nums:
            if val > 0 : sub_seq_sum+=val

    return max_sum,sub_seq_sum



#nums1=[1,15,2,1,2,2,3,0,0,3]
nums1=[[-1,5],[-5,5, -5],[-2,-3,-1,-4,-6],[3,4,-1,1,2],[1,15,2,1,2,2,3,0,0,3]]
for arr in nums1:
    print(arr,':',maxSubArray(arr))

for arr in nums1:
    best_seq_sum,sub_seq_sum=maxSubArray1(arr)
    print(arr, ' best_seq_sum:',best_seq_sum, 'sub_seq_sum:',sub_seq_sum)