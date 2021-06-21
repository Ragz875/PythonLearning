def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        L, R = nums[:mid], nums[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

a=[-2,3,-5,-1,-5]
print('Original Array:',a)
mergeSort(a)
print(a)