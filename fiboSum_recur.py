#code to find sum of fibonacci series
n=int(input("Enter a number to find its fibo sum "))
def fiboSum(n):
    if n<0:
        return 'Please enter positive integer '
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fiboSum(n-1) + fiboSum(n-2)

print(fiboSum(n))