

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
    if i%arr[0]==0 and i%arr[1]==0 and i%arr[2]==0:
        print(i)
