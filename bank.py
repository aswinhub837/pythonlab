class bank:
    def __init__(self,accno,name,acc_type,balance,amount):
        self.accno=accno
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
        self.amount=amount

    def deposit(self,amount):
        self.balance+=self.amount
        print("deposited successfully")
    def withdraw(self,amount):
        self.balance-=self.amount
        print("withdrawal successful")
    def display(self):
        print("account no:",self.accno)
        print("name",self.name)
        print("account type",self.acc_type)
        print("balance",self.balance)
        

accno=int(input("enter account number"))
name=input("enter name")
acc_type=input("enter account type")
balance=float(input("enter account balance"))
b=bank(accno,name,acc_type,balance,4500)    
b.display()  
b.deposit(4500)   
b.display()
b.withdraw(400)
b.display()  