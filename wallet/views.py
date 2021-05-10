from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from wallet.forms import WalletForm
from wallet.models import Wallet


class WalletDetail(FormMixin, DetailView):
    model = Wallet
    form_class = WalletForm
    # template_name = 'wallet/wallet_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class WalletList(ListView):
    model = Wallet

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.wallets.all()


class WalletUpdate(UpdateView):

    model = Wallet
    fields = ["name", "profile_pic", "default_currency"]

    def get_success_url(self):
        return reverse("wallet_detail", args=[self.object.id])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
