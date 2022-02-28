import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-.]+\.[A-Z|a-z]{2,}\b'
regex2 = r'\b[A-Za-z0-9.+-_%]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'

text = 'my name is sandesh and my emailid is sandesh.vora96@gm-ail.com and rohit96gupta@gmail.com'
mat =  re.findall(regex, text)
print(mat)
