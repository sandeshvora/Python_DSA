# #implementing queue using list
#
# queue=[]
# queue.append('a')
# queue.append('b')
# queue.append('c')
# print("Initial Queue")
# print(queue)
# queue.pop(0)
# print(queue)

#Implementing Queue using deque
from collections import deque
q=deque()
q.append('hi')
q.append('hello')
q.append('bye')
q.append('say')
q.popleft()
q.popleft()
print(q)