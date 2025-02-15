
from src.banken import Account

def test_deposit():
    my_account = Account(250)
    my_account.deposit(250)
    excepted = 500
    actual = my_account.balance()
    assert actual == excepted

def test_withdraw():
    my_account = Account(110)
    my_account.withdraw(50)
    excepted = 60
    actual = my_account.balance()
    assert actual == excepted

def test_balance():
    my_account = Account(75)
    excepted = 75
    actual = my_account.balance()
    assert actual == excepted

def test_apply_interest():
    my_account = Account(500)
    excepted = 525
    actual = my_account.apply_interest()
    assert actual == excepted

def test_afford():
    my_account = Account(5000)
    excepted_1 = True
    actual_1 = my_account.afford(5000)
    assert actual_1 == excepted_1
    actual_2 = my_account.afford(5001)
    excepted_2 = False
    assert actual_2 == excepted_2
