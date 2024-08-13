class employee:
    def __init__(self,name,id,bank_name,balance):
        self.name=name
        self.id=id
        self.bank_name=bank_name
        self.balance=balance

    def deposit(self,deposit):
        print(f"you are depositing {deposit} amt.")
        self.balance=self.balance+deposit
    
    def withdraw(self,withdraw):
        print(f"you are withdrawing {withdraw} amt.")
        self.balance=self.balance-withdraw

class display(employee):
    def show(self):
        print(f"your current balance in account is {self.balance}")

e1=display("souro","009","swift",1000000000)
e1.deposit(900000000)
e1.withdraw(60000)
e1.show()