from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from djmoney.contrib.exchange.models import convert_money
from djmoney.settings import CURRENCY_CHOICES
from djmoney.settings import DEFAULT_CURRENCY_CODE


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


UserModel = get_user_model()
# Create your models here.
class Wallet(TimeStampedModel):
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
    balance = models.DecimalField(
        max_digits=19,
        decimal_places=4,
        default=0,
        validators=[MinValueValidator(0.0001)],
    )

    def __str__(self):
        return f"{self.user.username} - {self.default_currency}"

    def credit(self, amount):
        # amount is a DJMOney MOneyField, so it has a currency attribute and a amountattribute
        try:
            converted_amount = convert_money(amount, self.default_currency)
            breakpoint()
            self.balance += converted_amount.amount
            res = self.save()
            return True
        except Exception as e:
            print(e.message)
            return False

    def debit(self, amount):
        # amount is a DJMOney MOneyField, so it has a currency attribute and a amountattribute
        try:
            converted_amount = convert_money(amount, self.default_currency)
            breakpoint()
            self.balance -= converted_amount.amount

            res = self.save()
            return True
        except Exception as e:
            print(e.message)
            return False
