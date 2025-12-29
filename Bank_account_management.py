class Member:
    def __init__ (self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance


    def show_details (self):
        print(self.account_no, self.holder_name,self.balance)


    def deposit(self,amount):
        self.balance = self.balance + amount 
        print("Amount deposite: " , amount)


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print("Amount withdrawn: " ,amount)

        else:
            print("Insufficient balance")



m1 = Member(123, "Harshveer", 100000)

m1.show_details()

m1.deposit(5000)
m1.withdraw(20000)

m1.show_details()
