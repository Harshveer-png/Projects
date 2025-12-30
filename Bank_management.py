class BankAccount:
    bank_name = "RUB"
    minimum_balance = 2500

    def __init__(self, account_holder_name, account_no, balance):
        if balance < BankAccount.minimum_balance:
            raise ValueError("Minimum balance 2500 required. Account not created.")

        self.name = account_holder_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.balance += amount
        print("Amount deposited:", amount)
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if self.balance - amount < BankAccount.minimum_balance:
            print("Withdrawal denied. Minimum balance must be maintained.")
            return

        self.balance -= amount
        print("Amount withdrawn:", amount)
        print("Remaining balance:", self.balance)

    def show_details(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)


c1 = BankAccount("Harshveer Kumar",125,2500)
c1.show_details()

print('-------------------------------------------------------------------------------')

c1.deposit (1500)
c1.withdraw (1000)

