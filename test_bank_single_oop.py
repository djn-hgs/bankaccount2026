import pytest

from bank_single_oop import Account


def test_create_with_default_balance():
    acc = Account("Andre")
    assert acc.balance == 0
    assert acc.owner == "Andre"


def test_create_with_initial_balance():
    acc = Account("Andre", 100)
    assert acc.balance == 100


def test_create_with_negative_balance_raises():
    with pytest.raises(ValueError):
        Account("Andre", -50)


@pytest.fixture
def account():
    return Account("Andre", 100)


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.get_balance() == 150


def test_deposit_zero_raises(account):
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative_raises(account):
    with pytest.raises(ValueError):
        account.deposit(-20)


def test_withdraw_decreases_balance(account):
    account.withdraw(40)
    assert account.get_balance() == 60


def test_withdraw_exact_balance_leaves_zero(account):
    account.withdraw(100)
    assert account.get_balance() == 0


def test_withdraw_more_than_balance_raises(account):
    with pytest.raises(ValueError):
        account.withdraw(150)


def test_withdraw_negative_raises(account):
    with pytest.raises(ValueError):
        account.withdraw(-10)
