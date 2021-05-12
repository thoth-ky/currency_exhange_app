from django.urls import reverse

from wallet.models import Wallet
from wallet.tests import CoreBaseTestCase


class WalletViewsTestCase(CoreBaseTestCase):
    def test__redirects_unlogged_user_(self):
        res = self.client.get(reverse("wallet_list"))
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/wallet/")

    def test_access_wallets_listfor_user(self):
        self.client.force_login(self.user1)
        res = self.client.get(reverse("wallet_list"))
        template_object_list = res.context_data["object_list"]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(template_object_list.count(), 1)
        self.assertQuerysetEqual(template_object_list, self.user1.wallets.all())

    def test_wallet_detail_view(self):
        self.client.force_login(self.user2)
        res = self.client.get(reverse("wallet_detail", args=[self.usd_wallet.id]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context_data["object"], self.usd_wallet)

    def test_wallet_detail_view_only_valid_user(self):
        self.client.force_login(self.user2)
        res = self.client.get(reverse("wallet_detail", args=[self.kes_wallet.id]))
        self.assertEqual(res.status_code, 403)

    def test_wallet_update_view(self):
        self.client.force_login(self.user2)
        new_name, new_currency = "Edited", "EUR"
        orig_bal_usd = self.usd_wallet.balance
        res = self.client.post(
            reverse("wallet_update", args=[self.usd_wallet.id]),
            {"name": new_name, "default_currency": new_currency},
        )

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, f"/wallet/{self.usd_wallet.id}")

        updated_wallet = Wallet.objects.get(id=self.usd_wallet.id)

        self.assertEqual(updated_wallet.name, new_name)
        self.assertEqual(updated_wallet.default_currency, new_currency)
        self.assertNotEqual(updated_wallet.balance, orig_bal_usd)

    def test_wallet_update_balance(self):
        self.client.force_login(self.user2)
        new_balance = 4000
        res = self.client.post(
            reverse("wallet_update", args=[self.usd_wallet.id]),
            {"balance": new_balance},
        )
        self.assertEqual(res.status_code, 200)
        updated_wallet, form = res.context_data["object"], res.context_data["form"]
        self.assertFalse(form.is_valid())
        self.assertNotEqual(updated_wallet.balance, new_balance)

    def test_wallet_update_only_valid_user(self):
        self.client.force_login(self.user2)
        res = self.client.post(
            reverse("wallet_update", args=[self.kes_wallet.id]), {"name": "Edited"}
        )
        self.assertEqual(res.status_code, 403)
