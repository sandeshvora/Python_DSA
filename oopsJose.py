class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __repr__(self):
        return f'{self.name},{self.author}'
    # def __str__(self):
    #     return "{}{}{}".format(self.author,self.name,self.pages)
    def __len__(self):
        return self.pages
    def __add__(self, other):
        return self.name+other
ab = Book("python","Sandesh",35)
cd =Book("java","sandy",45)
print(ab)
print(len(ab))
# del ab
print(ab)
print(ab+"geeks")
# lis = [3,4,9,6,7,5]
# lis2 = [i**2 for i in lis if i%2==0]
# print(lis2)
#
# abc1 =[1,2,3]
# dre = [6,7,8]
# abc1.extend(dre)
# print(abc1)