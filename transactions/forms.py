from django import forms

from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TransactionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Transaction
        fields = ("target_wallet", "txn_amount", "reference")

    def save(self, commit=True):
        breakpoint()
        return super().save(commit=commit)
