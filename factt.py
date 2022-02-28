n = int(input())
def facto(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res
print(facto(n))