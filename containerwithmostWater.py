def ContainerMostWater(arr):
    l=0
    r=len(arr)-1
    maxarea=0
    while(l<r):
        maxarea=max(maxarea,min(arr[l],arr[r])*(r-l))
        if (arr[l]<arr[r]):
            l+=1
        else:
            r-=1
    return maxarea

arr=[2,8,3,4,5,7,4]
print(ContainerMostWater(arr))