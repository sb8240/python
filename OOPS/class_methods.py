# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"the name is {self.name} and company is {self.company}")

#     def change_company(s, new_C): # first argument is self, by default it takes 1st argument as an instance
#         s.company = new_C

# e1 = Employee()
# e1.name = "name1"
# e1.show() # apple
# e1.change_company("mango")
# e1.show() # mango
# print(Employee.company) # apple

class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod # helps to change class variable
    def change_company(s, new_C): # now it will take 1st argument as class
        s.company = new_C

e1 = Employee()
e1.name = "name1"
e1.show() # apple
e1.change_company("mango")
e1.show() # mango
print(Employee.company) # mango