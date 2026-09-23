class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


def create_account(owner, balance=0):
    """Return a new account dict for owner, with the given starting balance.

    Should raise ValueError if balance is negative.
    """
    if balance < 0:
        raise ValueError

    return {
        "owner": owner,
        "balance": balance,
    }


def deposit(account, amount):
    """Add amount to account's balance.

    Should raise ValueError if amount is not positive.
    """
    if amount <= 0:
        raise ValueError

    account["balance"] += amount


def withdraw(account, amount):
    """Remove amount from account's balance.

    Should raise ValueError if amount is not positive, or if amount
    is more than the account's current balance.
    """
    account["balance"] -= amount


def get_balance(account):
    """Return account's current balance."""
    return account["balance"]
