#move zeroes to last with sorted array

def sortzero(arr):
    arr1 = arr[::-1]
    left =0
    right=0
    for i in range(len(arr)):
        if arr[i]!=0:
            right+=1
    slice_part = arr1[left:right][::-1]
    rem_part = arr1[right:]
    res = slice_part + rem_part
    print(res)


if __name__=='__main__':
    arr = [0,0,1,3,12]
    sortzero(arr)