import logging

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase

from wallet.models import Wallet
from wallet.tasks import update_exchange_rates


logging.disable(logging.WARNING)

User = get_user_model()


class CoreBaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):

        super().setUpClass()
        update_exchange_rates()
        cls.client = Client()

        cls.user1 = User.objects.create(username="user1", password="testpassword")

        cls.user2 = User.objects.create(username="user2", password="testpassword")

        cls.kes_wallet = Wallet.objects.create(
            name="TestWallet-KES", default_currency="KES", user=cls.user1, balance=100
        )

        cls.usd_wallet = Wallet.objects.create(
            name="TestWallet-USD", default_currency="USD", user=cls.user2, balance=10
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
