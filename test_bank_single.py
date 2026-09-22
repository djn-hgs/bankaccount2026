import pytest

from bank_single import create_account, deposit, withdraw, get_balance


def test_create_with_default_balance():
    acc = create_account("Andre")
    assert get_balance(acc) == 0
    assert acc["owner"] == "Andre"


def test_create_with_initial_balance():
    acc = create_account("Andre", 100)
    assert get_balance(acc) == 100


def test_create_with_negative_balance_raises():
    with pytest.raises(ValueError):
        create_account("Andre", -50)


@pytest.fixture
def account():
    return create_account("Andre", 100)


def test_deposit_increases_balance(account):
    deposit(account, 50)
    assert get_balance(account) == 150


def test_deposit_zero_raises(account):
    with pytest.raises(ValueError):
        deposit(account, 0)


def test_deposit_negative_raises(account):
    with pytest.raises(ValueError):
        deposit(account, -20)


def test_withdraw_decreases_balance(account):
    withdraw(account, 40)
    assert get_balance(account) == 60


def test_withdraw_exact_balance_leaves_zero(account):
    withdraw(account, 100)
    assert get_balance(account) == 0


def test_withdraw_more_than_balance_raises(account):
    with pytest.raises(ValueError):
        withdraw(account, 150)


def test_withdraw_negative_raises(account):
    with pytest.raises(ValueError):
        withdraw(account, -10)
