# mro -> method resolution oder

class Dance:

    def __init__(self, dance) -> None:
        self.dance = dance

    def show(self):
        print(f"the dance is {self.dance}")


class Dancer:
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
        print(f"the name of dancer is {self.name}")

class DancerEmp(Dance, Dancer):
    def __init__(self, dance, name) -> None:
        self.dance = dance
        self.name = name

obj1 = DancerEmp("xyz", "name1")
print(obj1.name)
print(obj1.dance)
obj1.show()
print(DancerEmp.mro())