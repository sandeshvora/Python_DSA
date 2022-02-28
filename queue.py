# Python code to implement queue
class queue:
    def __init__(self):
        self.q = []
    def push(self,x):
        self.q.append(x)
    def pop(self):
        self.q.pop(0)
    def peek(self):
        return self.q[0]

qu = queue()
qu.push(78)
qu.push(43)
qu.push(74)
print(qu.peek())
qu.pop()
qu.pop()
print(qu.peek())