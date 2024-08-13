# # constructors are of two types: 1) parameterised constructors and 2) default constructors

class Person:

    def __init__(self, name, occupation): # It is a constructor, It returns None
        self.name = name
        self.occupaiton = occupation

    def info(self):
        print(f"{self.name} is a {self.occupaiton}")

a= Person("souro", "enterprenuer")
a.info()