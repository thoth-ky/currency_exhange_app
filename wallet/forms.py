from django import forms

from wallet.models import Wallet


class WalletForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WalletForm, self).__init__(*args, **kwargs)
        self.fields["balance"].disabled = True

    class Meta:
        model = Wallet
        fields = ("name", "profile_pic", "default_currency", "balance")
