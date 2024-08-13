# operator overloading is a feature in python that allows developers to redefine the behaviour of mathematical and comparison operators for custom data types.


class Vector:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vector(self.i+x.i, self.j+x.j, self.k+x.k)

v1 = Vector(3, 7 ,9)
print(v1)

v2 = Vector(5, 6, 3)
print(v2)

print(v1+v2)
print(type(v1+v2))

