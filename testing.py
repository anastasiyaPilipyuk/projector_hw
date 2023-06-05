'''
Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method.
Ensure that the account is opened and has balance.
Test update method. It should check that code added interest and sended a message (print function was called).
'''

from mock import patch

from account_class import Account
from inheritance import Bank, SavingsAccount, CurrentAccount


# Test for the open_account method
def test_open_account():
    bank = Bank("Raiffeisen")
    account1 = Account(300, "ACCOUNT1")
    bank.open_account(account1)

    assert len([item for item in bank.get_bank_accounts()
                if item.get_account_number() == account1.get_account_number()]) == 1
    assert account1.get_balance() == 300


# Test for the update method
def test_update_method():
    bank = Bank("Raiffeisen")
    savings_account = SavingsAccount(1000, "SAVING1", 1.5)
    current_account = CurrentAccount(500, "CURRENT1", -100)

    bank.open_accounts([savings_account, current_account])

    # Perform some transactions to simulate account activity
    savings_account.add_interest()
    current_account.withdraw(700)

    with patch("builtins.print") as mock_print:
        bank.update()

    # Check that the interest was added to the savings account
    assert savings_account.get_balance() == 1030.22

    expected_message = f"Your account by number {current_account.get_account_number()}: is overdraft."
    # Check overdraft message was printed for the current account
    mock_print.assert_called_with(expected_message)


# Run the tests
test_open_account()
test_update_method()
