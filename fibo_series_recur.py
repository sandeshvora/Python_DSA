# code to find fibonacci series using recursion

n=int(input("Enter a number to display fibo series "))

def fiboSeries(n):
    if n<0:
        print('Please enter positive integer ')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fiboSeries(n-1) + fiboSeries(n-2)

for i in range(n):
    print(fiboSeries(i))