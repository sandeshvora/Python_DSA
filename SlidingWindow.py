arr=[80,-50,90,100]
k=2
def maxSum(arr,windowsize):
    arraysize=len(arr)
    if (arraysize<=windowsize):
        print("invalid operation")
    window_sum=sum(arr[i] for i in range(windowsize))


answer = maxSum(arr,k)
print(answer)
