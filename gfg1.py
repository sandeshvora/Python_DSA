

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a//gcd(a,b))*b








#find numbers between L and R which is divisible by all array elements

arr=[3,5,12]
l=90
r=280
for i in range(l,r):
    if all(i%item==0 for item in arr):
        print(i)
