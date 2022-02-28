class queue:
    def __init__(self):
        self.st = []
    def push(self,value):
        self.st.append(value)
    def pop(self):
        self.st.pop(0)
    def print(self):
        print(self.st)

q = queue()

q.push(67)
q.push(98)
q.push(2)
q.pop()
q.print()

