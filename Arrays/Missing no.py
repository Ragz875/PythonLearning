# Given an array nums containing n distinct numbers in the range [0, n], return the
# only number in the range that is missing from the array

if __name__ == '__main__':
    nums = [0,1,3,4]
    missing = len(nums)

    for i in range(len(nums)):
        print(i, ' ^= ', i, ' ^ ', nums[i])
        missing ^= i ^ nums[i]
        print(missing)
    print('missing number is:',missing)

