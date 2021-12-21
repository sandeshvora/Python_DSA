from typing import List
class Solution:
    def getLeftPosition(self,nums,target):
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]==target):
                if(nums[mid]==0 or nums[mid-1]!=target and mid-1>=0):
                    return mid
                right=mid-1
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1

    def getRightPosition(self,nums,target):
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]==target):
                if(mid==len(nums)-1 or nums[mid+1]!=target and mid+1<len(nums)):
                    return mid
                left=mid+1
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1

    def FirstAndLastOccurence(self,nums:List[int],target:int) -> List[int]:
        left = self.getLeftPosition(nums,target)
        right = self.getRightPosition(nums,target)
        return [left,right]

s=Solution()
print(s.FirstAndLastOccurence((1,2,2,3,4,4,4,4),4))
