#
n= int(input("Enter a positive number "))
res=0
while(n%2!=0):
    res+=n
    n=int(input("Enter again "))
if n%2==0:
    print("Woahh its even so final answer is",res*n)
