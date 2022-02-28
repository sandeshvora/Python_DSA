#cupcakes
cal = [5,10,7]
cal = sorted(cal,reverse=True)
res=0
for i in range(len(cal)):
    res+=(pow(2,i))*cal[i]
print(res)