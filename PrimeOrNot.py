#code to find if inp is prime or not
from datetime import datetime
start=datetime.now()
n=int(input("Enter a number is prime or not "))

if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print("its not prime number")
            break
    else:
        print("it is a prime number")

end=datetime.now()

print("execution time is",str(end-start)[5:])