#Brandon Washington

class BankAccount:
    
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("You deposited: " + str(amount))
        print("New balance: " + str(self.balance))
        print("-----------------------------------")
        
    def withdraw(self, amount):
        self.amount = amount
        self.balance = self.balance - amount
        print("You withdrew: " + str(amount))
        print("Your new balance is: " + str(self.balance))
        print("-----------------------------------")
        if(amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        
    def display_account_info(self):
        print("Balance: " + str(self.balance))
        print("-----------------------------------")
        
    def yield_interest(self):
        if(self.balance > 0):
            print("Balance before yield interest: "+ str(self.balance))
            self.balance = self.balance + (self.balance * self.int_rate)
            print("Balance after yield interest: " + str(self.balance))
            
    @classmethod        
    def show_all_accounts(cls):
        account_number = 1
        for account in cls.all_accounts:
            print("Account " + str(account_number)+ " = interest rate: "+ str(account.int_rate) + " balance: "+ str(account.balance))
            account_number+=1

class User:
    def __init__(self, name, email, Account):
        self.name = name
        self.email = email
        self.account = Account
    
    def make_deposit(self, amount, Account):
        self.account = Account
        self.account.deposit(amount)
        
    def make_withdraw(self,amount, Account):
        self.account = Account
        self.account.withdraw(amount)
        
    def display_user_balance(self, Account):
        self.account = Account
        self.account.display_account_info()
        



account1 = BankAccount(0.04, 2000)
account2 = BankAccount(0.09, 400)

account1.deposit(120)
account1.deposit(400)
account1.deposit(240)
account1.withdraw(300)
account1.yield_interest()
account1.display_account_info()

account2.deposit(40)
account2.deposit(650)
account2.withdraw(40)
account2.withdraw(60)
account2.withdraw(20)
account2.withdraw(90)
account2.yield_interest()
account2.display_account_info()

user1 = User("Brandon","Brandon@gmail.com",account1)
user1.make_deposit(100, account1)
user1.make_withdraw(50, account2)
user1.display_user_balance(account1)
user1.display_user_balance(account2)

BankAccount.show_all_accounts()