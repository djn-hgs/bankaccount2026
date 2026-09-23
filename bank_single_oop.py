class Account:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError
        self.balance -= amount

    def get_balance(self):
        return f'Owner {self.owner}, Balance: {self.balance}'

