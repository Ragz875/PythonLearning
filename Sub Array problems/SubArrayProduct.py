# this is a two pointer approach where Left and right pointing to 0 position
# right is incremented as long as cumulative product is < K (target)
# as soon as cum prod reaches K the move the left pointer but decrease cumulative product as (prev left) the count
# is redecued and need to adjust cum product
def subArrayProductLessthanK(nums,k):
    left=right=0
    prod=1
    # where sub array count is stored (where sub array prod < 100)
    result=0

    if k <=1: return 0

    while right < len(nums):
        prod *= nums[right]
        print(f'prod *= nums[right] : {prod} *= nums[{right}]')
        while prod >= k:
            prod = prod//nums[left]
            left+=1

        result += right - left + 1
        right = right + 1

    return result

# below problem without K
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and
# return the product. Array may contain -ves . Different logic to be used
def maxProdSubarry(nums):

    # copying in reverse way
    nums1=nums[::-1]

# this loop multiplies current value with previous value when previous value !=0
    for i in range(1,len(nums)):
        if nums[i-1] !=0 :  nums[i] *= nums[i-1]
        if nums1[i-1]!=0 :  nums1[i] *= nums1[i-1]

    # now you have two modified arrays , just return the max of two arrays
    return max(nums + nums1)

    print('result maxProdSubarry:', result)

print(subArrayProductLessthanK([10,5,2,6],100))
print(maxProdSubarry([2,3,-2,4]))