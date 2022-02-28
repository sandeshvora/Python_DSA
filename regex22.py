import re

regex1 = r'\b[A-Za-z0-9._%+-@[A-Za-z0-9-.]+\.[A-z|a-z]{2,}\b'
text = 'my name is sandesh and my email id is sandesh.vora96@gmail.com and rohit@gmail.com'
mat = re.findall(regex1, text)
print(mat)
