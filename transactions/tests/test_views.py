from django.urls import reverse
from djmoney.money import Money

from transactions.models import Transaction
from wallet.tests import CoreBaseTestCase


class TransactionView(CoreBaseTestCase):
    def test_transaction_form_fields_required(self):
        self.client.force_login(self.user1)
        balance, currency = self.kes_wallet.balance, self.kes_wallet.default_currency

        res = self.client.post(
            reverse("new_transaction", args={self.kes_wallet.id}), {}
        )

        self.assertFormError(res, "form", "reference", "This field is required.")
        self.assertFormError(res, "form", "txn_amount", "This field is required.")
        self.assertFormError(res, "form", "target_wallet", "This field is required.")

    def test_cash_transfer_above_balance(self):
        self.client.force_login(self.user1)

        self.client.post(
            reverse("new_transaction", args={self.kes_wallet.id}),
            {
                "target_wallet": self.usd_wallet.id,
                "txn_amount_0": 300,
                "txn_amount_1": "EUR",
                "reference": "Testing rsn",
            },
        )

        txn = Transaction.objects.last()
        self.assertEqual(txn.source_wallet, self.kes_wallet)
        self.assertEqual(txn.target_wallet, self.usd_wallet)
        self.assertEqual(txn.status, "DECLINED")

    def test_cash_transfer_within_balance(self):

        # LOad cash to source
        amount = Money(300, "EUR")
        res = self.kes_wallet.credit(amount)

        self.client.force_login(self.user1)

        balance = self.kes_wallet.balance
        usd_balance = self.usd_wallet.balance

        self.client.post(
            reverse("new_transaction", args={self.kes_wallet.id}),
            {
                "target_wallet": self.usd_wallet.id,
                "txn_amount_0": 200,
                "txn_amount_1": "EUR",
                "reference": "Testing rsn",
            },
        )

        txn = Transaction.objects.last()
        self.assertEqual(txn.source_wallet, self.kes_wallet)
        self.assertEqual(txn.target_wallet, self.usd_wallet)
        self.assertEqual(txn.status, "SUCCESS")

        self.assertLess(txn.source_wallet.balance, balance)
        self.assertGreater(txn.target_wallet.balance, usd_balance)
