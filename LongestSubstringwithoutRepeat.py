arr="fivestarreview"
def LongestSubNoRepeat(arr):
    m={}
    left=0
    right=0
    ans=0
    n=len(arr)
    while(left<n and right<n):
        element=arr[right]
        if element in m:
            left = max(left,m[element]+1)
        m[element]=right
        ans=max(ans,right-left+1)
        right+=1
    return ans

print(LongestSubNoRepeat(arr))


