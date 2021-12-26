def Partition(start,end,arr):
    pivot_index=start
    pivot=arr[pivot_index]

    while(start<end):
        while( start<len(arr) and arr[start]<= pivot):
            start+=1
        while(arr[end]>pivot):
            end-=1
        if (start<end):
            arr[start],arr[end]=arr[end],arr[start]
    arr[end],arr[pivot_index]=arr[pivot_index],arr[end]
    return end

def Quicksort(start,end,arr):
    if(start<end):
        p =Partition(start,end,arr)
        Quicksort(start,p-1,arr)
        Quicksort(p+1,end,arr)

arr=[7,4,1,3,9,24,87,45]
Quicksort(0,len(arr)-1,arr)
print(arr)

