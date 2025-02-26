class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print("Depositing $", amount, "...")
    
    def withdraw(self, amount):
        if self.__balance < amount:
            print("You do not have enough to withdraw $", amount)
        else: 
            self.__balance -= amount
            print("One moment while we withdraw $", amount,"from your account...")
    
    def get_balance(self):
        return self.__balance
    

B1 = BankAccount(100)
print("Initial balance: $" , B1.get_balance())
B1.deposit(200)
print("After deposit: $" , B1.get_balance())
B1.withdraw(150)
print("After first withdrawal: $" , B1.get_balance())
B1.withdraw(400)
print("Final balance: $" , B1.get_balance())
