#Phone Number - letter combination - Backtracking
class Solution:
    def backtracking(self,ans,m,digits,combination,index):
        if(index>len(digits)):
            return
        if(len(combination)==len(digits)):
            ans.append(combination[:])
            return ans
        currentDigit = digits[index]
        curString = m[currentDigit]

        for i in range(len(curString)):
            self.backtracking(ans,m,digits,combination + curString[i],index+1)
    def letterCombination(self,digits:str):
        ans = []
        if(len(digits)==0):
            return ans
        m = {}
        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "xyz"
        self.backtracking(ans,m,digits,"",0)
        print(ans)
        return ans
s=Solution()
s.letterCombination("964")