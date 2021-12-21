def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums),nums
print(removeElement([1,5,2,2,8,9,3],2))