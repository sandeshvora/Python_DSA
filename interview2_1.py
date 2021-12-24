#count number of odd digits in given list
def OddDigits(nums):
    count=0
    for i in nums:
        digits=0
        while(i>0):
            i//=10
            digits+=1
        if digits%2!=0:
            count+=1
    return count




print(OddDigits([66,444,3,22,999,888]))