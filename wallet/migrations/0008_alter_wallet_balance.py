# Generated by Django 3.2.2 on 2021-05-10 10:37
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0007_auto_20210510_0816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="balance",
            field=models.DecimalField(
                decimal_places=4,
                default=0,
                max_digits=19,
                validators=[django.core.validators.MinValueValidator(0.0001)],
            ),
        ),
    ]
