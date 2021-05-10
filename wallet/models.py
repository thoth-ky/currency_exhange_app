from django.contrib.auth import get_user_model
from django.db import models
from djmoney.settings import CURRENCY_CHOICES
from djmoney.settings import DEFAULT_CURRENCY_CODE

from wallet.utils.currencies import list_currency_choices


# CURRENCY_CHOICES = list_currency_choices()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


UserModel = get_user_model()
# Create your models here.
class Wallet(models.Model):
    name = models.CharField(max_length=25, verbose_name="Wallet Name")
    profile_pic = models.ImageField(
        upload_to="profiles/", null=True, blank=True, verbose_name="Profile Picture"
    )
    default_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=DEFAULT_CURRENCY_CODE,
        verbose_name="Default Currency",
    )
    user = models.ForeignKey(
        UserModel, on_delete=models.SET(get_sentinel_user), related_name="wallets"
    )
    balance = models.DecimalField(max_digits=19, decimal_places=4, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.default_currency}"

    def credit(self, amount):
        # amount is a DJMOney MOneyField, so it has a currency attribute and a amount attribute
        pass

    def debit(self, amount):
        pass
