"""
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1
has a size equal to m + n such that it has enough space to hold additional elements from nums2.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
hints: 3 pointer approach on one loop
"""
nums1,m = [4,5,0,0,0],2
nums2,n = [1,2,3], 3
print(nums1)
print(nums2)
p1=m-1
p2=n-1

for p in range(m+n-1,-1,-1):
    #if p2 < 0:
    #    break
    if nums1[p1] > nums2[p2] and p1 >= 0:
        nums1[p]=nums1[p1]
        p1=p1-1
    else:
        nums1[p]=nums2[p2]
        p2=p2-1
        if p2 < 0:
            break

print(nums1,p1,p2)
