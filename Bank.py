class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.transaction_history = []

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        else:
            print("Error: Amount must be positive")
            return False
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount}")
                return True
            else:
                print("Error: Insufficient funds")
                return False
        else:
            print("Error: Amount must be positive")
            return False

    def get_transaction_history(self):
        return self.transaction_history

class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, balance=0, interest_rate=0.02):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.__balance * self.interest_rate
        self.__balance += interest
        self.transaction_history.append(f"Interest Added: +${interest:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, name, account_number, balance=0, overdraft_limit=100):
        super().__init__(name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance + self.overdraft_limit >= amount:
                self.__balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount}")
                return True
            else:
                print("Error: Exceeds overdraft limit")
                return False
        else:
            print("Error: Amount must be positive")
            return False

if __name__ == "__main__":
    
    savings = SavingsAccount("John Doe", "SAV001", 1000)
    checking = CheckingAccount("John Doe", "CHK001", 500)

    print("Initial balances:")
    print(f"Savings: ${savings.get_balance()}")
    print(f"Checking: ${checking.get_balance()}")

    savings.deposit(200)
    print("\nAfter depositing $200 to savings:")
    print(f"Savings: ${savings.get_balance()}")

    checking.withdraw(100)
    print("\nAfter withdrawing $100 from checking:")
    print(f"Checking: ${checking.get_balance()}")

    savings.add_interest()
    print("\nAfter adding interest to savings:")
    print(f"Savings: ${savings.get_balance()}")

    print("\nSavings Account Transaction History:")
    for transaction in savings.get_transaction_history():
        print(transaction)

