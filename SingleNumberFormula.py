def SingleNumberNaive(nums):
    summation=0
    res=set()
    solution=0
    for i in range(len(nums)):
        summation+=nums[i]
    for k in nums:
        res.add(k)
    abc=sum(res)*2
    solution= abc-summation
    return solution



print(SingleNumberNaive([1,1,2,2,8]))

#one liner --> return 2*sum(set(nums))-sum(nums)