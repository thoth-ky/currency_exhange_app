# Generated by Django 3.2.2 on 2021-05-10 09:47
import django.db.models.deletion
import djmoney.models.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0007_auto_20210510_0816"),
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="reference",
            field=models.CharField(
                help_text="Narration e.g Water Bill",
                max_length=250,
                verbose_name="Reason for Transfer",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="source_wallet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="send",
                to="wallet.wallet",
                verbose_name="Send From",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="target_wallet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="receive",
                to="wallet.wallet",
                verbose_name="Send To",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="txn_amount",
            field=djmoney.models.fields.MoneyField(
                decimal_places=4, max_digits=19, null=True, verbose_name="Amount"
            ),
        ),
    ]
