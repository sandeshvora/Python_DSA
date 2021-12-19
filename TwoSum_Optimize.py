#leetcode first problem optimize O(n) solution

def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

nums=[11,12,15,17]
print(twoSum(nums,29))
