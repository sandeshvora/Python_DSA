#factorial of number using recursion

n=int(input("Enter a number to find it's factorial"))
def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)

print(fact(n))
