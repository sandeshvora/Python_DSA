arr=[11,12,13,14,15]
target = 14

def binarySearch(arr,target):
    start = 0
    end=len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            start = mid+1
        else:
            end = mid-1
    return -1

result = binarySearch(arr,target)
if result!=-1:
    print("element is present in array at index",result)
else:
    print("element is not present in array at index")
