arr=[80,-50,90,100]
k=2
def maxSum(arr,windowsize):
    arraysize=len(arr)

    if (arraysize<=windowsize):
        print("invalid operation")


    window_sum=sum(arr[i] for i in range(windowsize))
    max_sum = window_sum

    for i in range(arraysize-windowsize):
        window_sum = window_sum - arr[i]+arr[i+windowsize]
        max_sum = max(window_sum,max_sum)
    return max_sum

answer = maxSum(arr,k)
print(answer)
