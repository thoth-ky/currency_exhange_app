# Generated by Django 3.2.2 on 2021-05-10 11:15
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0004_auto_20210510_1112"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["created"]},
        ),
    ]
