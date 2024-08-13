class Owner:
    class_variable = "c++"
    no_of_employees = 0 #an exp of using class variable
    def __init__(self, name) -> None:
        self.name = name
        self.instance_variable = "python"
        Owner.no_of_employees += 1
    def show_details(self):
        print(f"the name of the owner {self.no_of_employees} is {self.name} and language is {self.instance_variable} and class_v is {self.class_variable}")
    
o1 = Owner("souro")
#both are two different types of method for changing class and instance variable
Owner.class_variable = "java"
o1.instance_variable = "ruby"
# first the program will search for the instance variable and then search for class variable
o1.show_details() # we can also use Owner.show_details(o1)
o2 = Owner("linux")
o2.show_details()