#Insertion Sort
arr = [7,2,6,9,1]
def Insert(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while(arr[j]>current and j>=0):
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]=current
    return arr
print(Insert(arr))
