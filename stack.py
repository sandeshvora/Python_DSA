#Python code to implement stack
class stack:
    def __init__(self):
        self.st = []
    def push(self,x):
        self.st.append(x)
    def pop(self):
        self.st.pop()
    def peek(self):
        return self.st[-1]

s = stack()
s.push(57)
s.push(89)
s.push(51)

print(s.peek())
s.pop()
print(s.peek())