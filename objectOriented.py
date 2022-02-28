#object oriented programming in python

#classes and Objects
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_details(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("I am a Person",self.name,"and age is",self.age)
    def greet(self):
        print("how are you doing?",self.age)
        self.display()

p2 = Person('sandy',76)
p2.set_details('sandesh',55)
p2.display()

#super().__init__(name,age,address,phone)
#super().contact_details()