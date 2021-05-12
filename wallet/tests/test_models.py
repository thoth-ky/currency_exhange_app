from djmoney.money import Money

from wallet.models import Wallet
from wallet.tests import CoreBaseTestCase


class WalletModelTestCase(CoreBaseTestCase):
    def test_dummy(self):
        assert Wallet.objects.count() == 2

    def test_can_credit_wallet(self):
        amount = Money(300, "KES")

        res = self.kes_wallet.credit(amount)
        self.assertTrue(res)
        self.assertEqual(400, self.kes_wallet.balance)

        amount = Money(300, "USD")

        orig_bal = self.kes_wallet.balance
        res = self.kes_wallet.credit(amount)
        self.assertTrue(res)
        self.assertGreater(self.kes_wallet.balance, orig_bal)

    def test_can_debit_amount(self):
        amount = Money(300, "KES")
        exp_balance = self.kes_wallet.balance - 300

        res = self.kes_wallet.debit(amount)
        self.assertTrue(res)
        self.assertEqual(exp_balance, self.kes_wallet.balance)

        amount = Money(300, "USD")

        orig_bal = self.kes_wallet.balance
        res = self.kes_wallet.debit(amount)
        self.assertTrue(res)
        self.assertLess(self.kes_wallet.balance, orig_bal)

        more_than_bal = self.kes_wallet.balance + 200

        amount = Money(more_than_bal, "KES")
        res = self.kes_wallet.debit(amount)
        self.assertFalse(res)
