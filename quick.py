def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]
    while(start<end):
        while(start <len(arr) and arr[start]<= pivot):
            start +=1
        while(arr[end]>pivot):
            end -=1
        if(start<end):
            arr[start],arr[end] = arr[end],arr[start]
    arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
    return end
def quicksort(start, end, arr):
    if(start < end):
        p = partition(start,end,arr)
        quicksort(start,p-1,arr)
        quicksort(p+1,end,arr)
arr = [2,4,7,1,55,33,11]
start = 0
end =len(arr) -1
quicksort(start,end,arr)
print(arr)