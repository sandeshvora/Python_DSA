def decs(func):
    def wrapper(*args):
        res = func(*args).upper()
        return res
    return wrapper
# ab='sandy'
x= 'bro'
@decs
def sandesh(x):
    return x
print(sandesh(x))
#
# def teen(n):
#     if n in [13,14,17,18]:
#         return 0
#     return n
# # print(teen(14))
# a=[3,4,1,2,6,8,50]
# b = list(filter(lambda x:(x%2==0),a))
# print(b)
# a=[3,4,1,2,6,8,50]
# b = list(map(lambda x:x**2,a))
# print(b)