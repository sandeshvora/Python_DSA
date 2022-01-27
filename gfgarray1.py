# Reverse The Array

def ReverseArray(arr,start,end):
    n= len(arr)
    start = 0
    end = n - 1
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end-=1
    return arr

# Driver Code
arr = [5,8,2,44,66]
print(ReverseArray(arr,0,4))