from django.db.models.signals import post_save
from django.dispatch import receiver

from transactions.models import Transaction


@receiver(post_save, sender=Transaction)
def update_wallets(sender, **kwargs):
    instance = kwargs.get("instance")
    created = kwargs.get("created")

    if created:
        source_currency = instance.source_wallet.default_currency
        target_currency = instance.target_wallet.default_currency

        debit_success = instance.source_wallet.debit(instance.txn_amount)
        credit_success = False

        if debit_success:
            credit_success = instance.target_wallet.credit(instance.txn_amount)

        if not credit_success:
            # reverse source debit
            instance.source_wallet.credit(instance.txn_amount)
            breakpoint()
            instance.status = "DECLINED"
        else:
            instance.status = "SUCCESS"
        instance.save()
