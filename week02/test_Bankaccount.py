import unittest

from week02.BankAccount import BankAccount

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Me", 1234, 100)

    def test_deposit(self):
        original_balance = self.account.balance
        self.account.deposit(-20)
        self.assertEqual(self.account.balance, original_balance)
        self.account.deposit(0)
        self.assertEqual(self.account.balance, original_balance)
        self.account.deposit(100)
        self.assertEqual(self.account.balance, original_balance + 100)

    def test_withdraw(self):
        original_balance = self.account.balance
        self.account.withdraw(original_balance+20)
        self.assertEqual(self.account.balance, original_balance)
        self.account.withdraw(original_balance-20)
        self.assertEqual(self.account.balance, 20)


if __name__ == '__main__':
    unittest.main()