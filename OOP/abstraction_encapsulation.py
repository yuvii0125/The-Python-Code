class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # Encapsulation: Hiding sensitive data (__balance) from outside access
        self.__balance = balance

    # Abstraction: Wrapping up a data and methods into a single object

    # Abstraction: Provides a simple way to deposit money without exposing balance details
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to balance")
        else:
            print("Deposit amount must be positive")

    # Abstraction: Provides a simple way to withdraw money without exposing balance details
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount} from balance")
            else:
                print("Insufficient funds")
        else:
            print("Withdraw amount must be positive")

    # Abstraction: Only shows the current balance without allowing direct access to __balance
    def get_balance(self):
        return self.__balance


# Example usage
account = Account("Yuvraj", 1000)
account.deposit(500)        # Deposits 500
account.withdraw(300)       # Withdraws 300
print("Current Balance:", account.get_balance())  # Retrieves current balance

# Attempting to access the private balance attribute directly will result in an error
# print(account.__balance)  # Uncommenting this line will raise an AttributeError
