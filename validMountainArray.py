def validMountain(n):
    i=1
    while(i<len(n) and n[i]> n[i-1]):
        i+=1
    if(i==1 or i == len(n)):
        return False
    while(i < len(n) and n[i]<n[i-1]):
        i+=1
    return i == len(n)


n=[1,2,3,4,3,2,1]
print(validMountain(n))