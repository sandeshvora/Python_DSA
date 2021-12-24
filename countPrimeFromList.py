def countPrime(list1):
    count=0
    for i in list1:
        if i > 1:
            for a in range(2, i // 2 + 1):
                if i % a == 0:
                    count+=1
                    break

    return count

print(countPrime([2,3,4,5,6,8]))