#Two sum first leet code problem - naive approach
# time complexity = O(n^2)
n=[2,6,4,24]
flag=False
target=int(input("please enter target "))
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if target-n[i]==n[j]:
            print(i,j)
            flag=True
if flag==False:
    print("No elements found")


