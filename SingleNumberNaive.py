def SingleNumberNaive(nums):
    for i in range(len(nums)):
        if nums.count(nums[i])==1:
            print(nums[i])



print(SingleNumberNaive([1,1,2,2,8]))