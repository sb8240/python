# # In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method."

class person:
    name = 'e.M'
    occupation = 'genius'
    networth = '$100b'

    def info(self): #method --> functions defined inside a class.
        print(f'{self.name} is a {self.occupation}') # self parameter is a reference to the current instance of the class, and is used to access variables that belolngs to the class.
        # self is that object for which this method is called.

a = person()
a.name='souro'
print(a.name)
print(a.occupation)

a.info()
