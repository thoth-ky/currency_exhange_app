from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField

from wallet.models import Wallet


TRANSACTION_STATUS = (
    ("PENDING", "PENDING"),
    ("SUCCESS", "SUCCESS"),
    ("DECLINED", "DECLINED"),
)


class Transaction(models.Model):
    source_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="send",
        verbose_name="Send From",
    )
    target_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="receive",
        verbose_name="Send To",
    )
    txn_amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        null=True,
        default_currency=None,
        verbose_name="Amount",
    )
    status = models.CharField(
        max_length=8, choices=TRANSACTION_STATUS, default="PENDING"
    )
    reference = models.CharField(
        max_length=250,
        help_text="Narration e.g Water Bill",
        verbose_name="Reason for Transfer",
    )

    def __str__(self):
        return f"{self.source_wallet} to {self.target_wallet} #{self.txn_amount}"
