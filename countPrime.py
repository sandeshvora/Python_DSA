def countPrime(nums):
    count=0
    countprime=0
    for a in range(2,nums+1):
        for i in range(2,a//2+1):
            if a % i == 0:
                count+=1
                break
        else:
            countprime+=1
    return countprime

print(countPrime(100))