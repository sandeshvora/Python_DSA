#Insertion Sort
arr = [7,6,10,8,9]
def Insert(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while(arr[j]>current and j>=0):
            arr[j+1]= arr[j] # Right shift
            j-=1
        arr[j+1]=current
    return arr
print(Insert(arr))
