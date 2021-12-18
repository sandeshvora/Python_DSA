# code to find fibonacci series using recursion
n=int(input("Enter a number to display fibo series "))

def fiboSeriess(n):
    if n<0:
        print('Please enter positive integer ')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fiboSeriess(n-1) + fiboSeriess(n-2)

for i in range(n):
    print(fiboSeriess(i))
