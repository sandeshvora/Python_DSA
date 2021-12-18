#leetcode first problem using 2 pointer method

def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

nums=[1,2,5,7]
print(twoSum(nums,9))
