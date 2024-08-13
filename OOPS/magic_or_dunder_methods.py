class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):
    print("Hey I am good")

e = Employee("Harry")
print(str(e))
print(repr(e))
# print(e.name)
# print(len(e))
e()

# The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor"
# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
# The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
# The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.