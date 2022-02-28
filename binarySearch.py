
arr = [1,3,4,5,6,7,9,11]
target = 7
def BinarySearch(arr,target):
    start = 0
    end = len(arr) -1
    while(start <= end):
        mid = (start+end)//2
        if(arr[mid] == target):
            return arr[mid]
        elif(arr[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return -1
res = BinarySearch(arr, target)
if res!=-1:
    print("found",res)
else:
    print("not found")
