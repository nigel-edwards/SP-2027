# Bank Account

class BankAccount:
    def __init__(self,
                 account_holder,
                 account_number,
                 balance):
        self._account_holder = account_holder
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
        else:
            print("Invalid amount - must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount - must be positive")
        elif amount > self._balance:
            print("Invalid amount - must be less than or equal to the current balance")
        else:
            self._balance -= amount

    def __str__(self):
        return (f"Account holder: {self._account_holder}, Account number: {self._account_number}, Balance: {self._balance}")

    @property
    def balance(self):
        return self._balance

def main():
    account = BankAccount("Me", 1234, 100)
    account.deposit(100)
    account.withdraw(10)
    print(account)

if __name__ == "__main__":
    main()

