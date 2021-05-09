from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField

from wallet.utils.currencies import list_currency_choices


CURRENCY_CHOICES = list_currency_choices()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


UserModel = get_user_model()
# Create your models here.
class Wallet(models.Model):
    profile_pic = models.ImageField(upload_to="profiles/", null=True, blank=True)
    default_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, blank=False, null=False
    )
    user = models.ForeignKey(UserModel, on_delete=models.SET(get_sentinel_user))
    balance = MoneyField(
        max_digits=19, decimal_places=4, null=True, default_currency=None
    )

    def __str__(self):
        return f"{self.user.username}- {self.default_currency}"

    def credit(self, amount, currency_code):
        pass

    def debit(self, amount, currency_code):
        pass
