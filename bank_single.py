"""Procedural bank account management — one account.

An account is just a dict: {"owner": ..., "balance": ...}.
Every function below takes that dict as its first argument.

Fill in each function so that test_bank_single.py passes.
"""


def create_account(owner, balance=0):
    """Return a new account dict for owner, with the given starting balance.

    Should raise ValueError if balance is negative.
    """
    raise NotImplementedError


def deposit(account, amount):
    """Add amount to account's balance.

    Should raise ValueError if amount is not positive.
    """
    raise NotImplementedError


def withdraw(account, amount):
    """Remove amount from account's balance.

    Should raise ValueError if amount is not positive, or if amount
    is more than the account's current balance.
    """
    raise NotImplementedError


def get_balance(account):
    """Return account's current balance."""
    raise NotImplementedError
