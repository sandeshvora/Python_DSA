#code for fibo series using naive approach but optimize space complexity

nterms=int(input('enter a number to display its fibonacci series'))
count=0
a,b=0,1
for i in range(nterms):
    while(count<nterms):
        print(a)
        c=a+b
        a=b
        b=c
        count+=1


