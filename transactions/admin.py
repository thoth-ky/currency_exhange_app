from django.contrib import admin

from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "source_wallet", "target_wallet", "txn_amount", "status")


admin.site.register(Transaction, TransactionAdmin)
