def BoatSaving(people,limit):
    people.sort()
    boatsnumber=0
    n=len(people)
    left=0
    right=len(people)-1
    while(left<=right):
        if(left==right):
            boatsnumber+=1
            break
        if(people[left]+people[right]<=limit):
            left+=1
            right-=1
            boatsnumber+=1
        else:
            right-=1
            boatsnumber+=1
    return boatsnumber

print(BoatSaving([1,2,2,3],3))

