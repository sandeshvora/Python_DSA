# Selection sort code
def SelectionSort(arr):
    size=len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if(arr[j]< arr[min_index]):
                min_index=j
        if(min_index!=i):
            arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

if __name__ == '__main__':
    arr=[8,5,1,2,9,4]
    SelectionSort(arr)
    print(arr)
