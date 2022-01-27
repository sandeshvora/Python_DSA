#lamba_obj = lambda x:x*x
#print(lamba_obj(3))
# list1=[1,5,7,8,3,5,22]
# list2=list1.copy()
# list2[-1]=101
# print(list1)
# print(list2)

# string = 'partlvlvlonestralvl'
# count=0
# for i in range(len(string)):
#    if string[i:i+3] == 'lvl':
#        count+=1
# print(count)

l=[[1 ,2, 3], [4, 5, 6], [7, 8, 9]]
a=[[row[i] for row in l] for i in range(3)]
print(a)



