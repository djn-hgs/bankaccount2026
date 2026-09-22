"""Procedural bank account management — many accounts, identified by account number.

A bank is a dict mapping account_number -> account dict
({"owner": ..., "balance": ...}). Every function takes the bank
and, where relevant, an account_number.

Fill in each function so that test_bank_multi.py passes.
"""


def create_bank():
    """Return a new, empty bank."""
    raise NotImplementedError


def open_account(bank, account_number, owner, balance=0):
    """Add a new account to bank under account_number.

    Should raise ValueError if account_number is already in use,
    or if balance is negative.
    """
    raise NotImplementedError


def deposit(bank, account_number, amount):
    """Add amount to the balance of the account at account_number.

    Should raise ValueError if amount is not positive.
    Should raise KeyError if account_number does not exist in bank.
    """
    raise NotImplementedError


def withdraw(bank, account_number, amount):
    """Remove amount from the balance of the account at account_number.

    Should raise ValueError if amount is not positive, or if amount
    is more than that account's current balance.
    Should raise KeyError if account_number does not exist in bank.
    """
    raise NotImplementedError


def get_balance(bank, account_number):
    """Return the current balance of the account at account_number.

    Should raise KeyError if account_number does not exist in bank.
    """
    raise NotImplementedError


def transfer(bank, from_account_number, to_account_number, amount):
    """Move amount from one account to another within bank.

    Should use withdraw and deposit rather than touching balances directly.
    """
    raise NotImplementedError
