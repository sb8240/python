'''
static methods in python are methods that belong to a class rather than an instance of the class. they are defined using the @staticmethod decorator and do not have access to the instance of the class(ie. self)
they are called on the class itself, not on an instance of the class
static methods are often used to create utility functions that dont need access to instance data
'''

class Math:
    def __init__(self, num) -> None:
        self.num = num
    def addtonum(self, n):
        self.num = self.num+n
    
    @staticmethod
    def add(a,b):
        return a+b

a = Math(9)
a.addtonum(6)
s = a.add(4,8)
print(s)
print(a.num)
