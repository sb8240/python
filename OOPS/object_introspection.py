# x={}
# print(dir(x))
# print(help(list))

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.version = 1

p = Person("souro",18)
print(p.__dict__)
print(help(Person))
print(p.__dir__)