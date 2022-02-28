import math
def countPrimeSieveofEratothenes(n):
    isPrime=[True]*n
    isPrime[0]=isPrime[1]=False
    if(n<2):
        return 0
    for i in range(2,math.ceil(math.sqrt(n))):
        if isPrime[i]:
            for k in range(i*i,n,i):
                isPrime[k]=False
    return sum(isPrime)

print(countPrimeSieveofEratothenes(10))
# 0 1
# 4 6 8
# 9
### 2 3 5 7
