def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
#code to print list
def PrintList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
#Driver Code
if __name__ == '__main__':
    arr = [11, 2, 4, 8, 9, 55, 3]
    print("Before sorting")
    PrintList(arr)
    print("After Sorting")
    MergeSort(arr)
    PrintList(arr)


