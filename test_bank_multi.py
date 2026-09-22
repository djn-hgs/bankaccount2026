import pytest

from bank_multi import (
    create_bank,
    open_account,
    deposit,
    withdraw,
    get_balance,
    transfer,
)


@pytest.fixture
def bank():
    b = create_bank()
    open_account(b, "001", "Andre", 100)
    open_account(b, "002", "Alex", 50)
    open_account(b, "003", "Viraj", 75)
    return b


def test_open_creates_account_with_balance():
    b = create_bank()
    open_account(b, "001", "Andre", 100)
    assert get_balance(b, "001") == 100


def test_open_default_balance_is_zero():
    b = create_bank()
    open_account(b, "002", "Alex")
    assert get_balance(b, "002") == 0


def test_duplicate_account_number_raises():
    b = create_bank()
    open_account(b, "001", "Andre", 100)
    with pytest.raises(ValueError):
        open_account(b, "001", "Viraj")


def test_negative_initial_balance_raises():
    b = create_bank()
    with pytest.raises(ValueError):
        open_account(b, "003", "Viraj", -50)


def test_deposit_affects_correct_account_only(bank):
    deposit(bank, "001", 25)
    assert get_balance(bank, "001") == 125
    assert get_balance(bank, "002") == 50
    assert get_balance(bank, "003") == 75


def test_withdraw_insufficient_funds_raises(bank):
    with pytest.raises(ValueError):
        withdraw(bank, "002", 100)


def test_unknown_account_number_raises_key_error(bank):
    with pytest.raises(KeyError):
        deposit(bank, "999", 10)
    with pytest.raises(KeyError):
        withdraw(bank, "999", 10)
    with pytest.raises(KeyError):
        get_balance(bank, "999")


def test_transfer_moves_money_between_accounts(bank):
    transfer(bank, "001", "002", 30)
    assert get_balance(bank, "001") == 70
    assert get_balance(bank, "002") == 80
    assert get_balance(bank, "003") == 75


def test_transfer_insufficient_funds_leaves_balances_unchanged(bank):
    with pytest.raises(ValueError):
        transfer(bank, "002", "001", 1000)
    assert get_balance(bank, "001") == 100
    assert get_balance(bank, "002") == 50
    assert get_balance(bank, "003") == 75
