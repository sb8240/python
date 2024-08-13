class Employee:
    def __init__(self, name, id) -> None:
        self.name = name 
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang) -> None:
        super().__init__(name, id)
        self.lang = lang

name1 = Employee("name1", "11001")
name2 = Programmer("name2", "10101", "english")

print(name2.name)
print(name2.id)
print(name1.name)
print(name1.id)
print(name2.lang)