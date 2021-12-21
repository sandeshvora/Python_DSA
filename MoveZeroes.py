def moveZeroes(nums):
    b = len(nums)
    j = 0
    for num in nums:
        if (num != 0):
            nums[j] = num
            j += 1
    for i in range(j, b):
        nums[i] = 0
    return nums

print(moveZeroes([1,0,5,0,2,3,]))