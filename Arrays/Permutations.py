def perm(index=0):
    # base case
    if index==len(nums):
        output.append(nums[::])
        return
    for i in range(index,len(nums)):
        #print(i,first)
        nums[index],nums[i]=nums[i],nums[index]
        perm(index+1)
        nums[index], nums[i] = nums[i], nums[index]
    #print(nums)
nums=[1,2,3]
output=[]
perm()
output.sort()
print(output)
