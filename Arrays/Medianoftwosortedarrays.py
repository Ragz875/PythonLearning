def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # Both lists are empty
    if len(nums1) == 0 and len(nums2) == 0:
        return 0

    if len(nums1) > 0 and len(nums2) == 0:
        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) // 2

    elif len(nums1) == 0 and len(nums2) > 0:
        if len(nums2) % 2 == 1:
            return nums2[len(nums2) // 2]
        else:
            return (nums2[len(nums2) // 2] + nums2[(len(nums2) // 2) - 1]) // 2
    else:
        tot_len = len(nums1) + len(nums2)
        nums3 = nums1 + nums2
        nums3.sort()
        if tot_len % 2 == 1:
            return nums3[tot_len // 2]
        else:
            return (nums3[tot_len // 2] + nums3[(tot_len // 2) - 1]) // 2
