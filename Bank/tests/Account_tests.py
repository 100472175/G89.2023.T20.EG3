import unittest
from unittest import TestCase
from Class_unittest_more.Bank.Account import Account
from Class_unittest_more.Bank.BankException import BankException

class TestAccount(TestCase):

    def setUp(self):
        self.mysource = Account(100)
        self.mydestination = Account(100)

    def tearDown(self):
        self.mysource = None
        self.mydestination = None

    def test_get_balance(self):
        balance = self.mysource.getBalance()
        self.assertEqual(balance, 100)

    def test_deposit(self):
        self.mysource.deposit(200)
        balance = self.mysource.getBalance()
        self.assertEqual(balance,300)

    def test_deposit_negative_value(self):
        with self.assertRaises(BankException) as cm:
            self.mysource.deposit(-200)
        self.assertEqual(cm.exception.__str__(), "Error the amount must be positive")

    def test_withdraw(self):
        self.mysource.withdraw (25)
        balance = self.mysource.getBalance()
        self.assertEqual(balance, 75)

    def test_withdraw_negative_value(self):
        try:
            self.mysource.withdraw(-200)
            self.fail("An exception must be raised!")
        except (BankException) as ex:
            self.assertEqual(ex.__str__(), "Error the amount must be positive")

    def test_withdraw_with_insufficient_funds(self):
        try:
            self.mysource.withdraw(120)
            self.fail("An exception must be raised!")
        except (BankException) as ex:
            self.assertEqual(ex.__str__(), "Error insufficient funds in the account")

    def test_transfer_funds(self):
        self.mysource.transferFunds(self.mydestination, 25)
        balance = self.mysource.getBalance()
        self.assertEqual(balance, 75)

    def test_transfer_funds_wrong(self):
        with self.assertRaises(BankException) as cm:
            self.mysource.transferFunds(self.mydestination, 300)
        self.assertEqual(cm.exception.__str__(), "Error, balance is minor than minimum balance")

if __name__ == '__main__':
    unittest.main()
