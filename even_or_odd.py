# code to check if number is even or odd
n=int(input("Enter a number to check if its even or odd "))
def evenOdd(n):
    if n%2==0:
        return 'its even'
    else:
        return 'its odd'

print(evenOdd(n))