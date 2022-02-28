class stack:
    def __init__(self):
        self.st = []
    def push(self,p):
        self.st.append(p)
    def pop(self):
        return self.st.pop()
    def peek(self):
        return self.st[-1]
    def print(self):
        print(self.st)
s =stack()
s.push(78)
s.push(77)
s.push(98)
s.pop()
print(s.peek())
s.print()