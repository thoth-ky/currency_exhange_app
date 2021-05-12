from django import forms

from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("target_wallet", "txn_amount", "reference")
