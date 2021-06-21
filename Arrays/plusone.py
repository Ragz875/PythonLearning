# with the help of str and int functions
def plusone_1(nums):
    print('plusone_1')
    nums_str=''.join([str(num) for num in nums])
    str_nums= int(nums_str) + 1
    if len(str(str_nums)) > 1:
        return [int(ch) for ch in str(str_nums)]
    else:
        return [str_nums]

# without using str and int, school maths
def plusone_2(nums):
    print('plusone_2')
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==9:
            nums[i]=0
        else:
            nums[i]+=1
            return nums
    return [1] + nums




if __name__== '__main__':
    print('Main started')
    a=[9]
    print(plusone_2(a))


