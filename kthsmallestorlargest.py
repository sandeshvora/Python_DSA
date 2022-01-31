#Python program to find an kth largest and smallest element
def Kminmax(arr,k):
    arr.sort()
    print(arr)
    min = arr[k-1]
    max = arr[-k]
    return min,max

if __name__ == '__main__':
    arr = [6,9,3,4,22,32,77,2]
    k=3 #3rd largest and smallest element in an array
    print(Kminmax(arr,k))