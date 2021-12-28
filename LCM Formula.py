#python LCM formula
# a * b = gcd(a,b) * lcm(a,b)...so,
# lcm(a,b) = (a*b)/gcd(a,b)

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a//gcd(a,b))*b
print(gcd(15,25))
print(lcm(15,25))