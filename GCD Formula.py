#GCD of two numbers using euclidean (modulo) operator -- more efficient

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(60,48))



# gcd using euclidean formula (subtract)

def gcdsub(a,b):
    if (a==0):
        return b
    if (b==0):
        return a
    #// base case
    if (a == b):
        return a
    if(a>b):
        return gcd(a-b,a)
    return gcd(a,b-a)
print("GCD is",end=" ")
print(gcdsub(98,56))
