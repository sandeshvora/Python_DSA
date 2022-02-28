#move zeroes to last with sorted array

def sortzero(arr):
    n = len(arr)
    output = []
    for i in range(len(arr)):
        if arr[i] !=0:
            output.append(arr[i])
    m = len(output)
    for i in range(m,n):
        output.append(0)
    print(output)



if __name__=='__main__':
    arr = [43,0,1,0,3,12]
    sortzero(arr)