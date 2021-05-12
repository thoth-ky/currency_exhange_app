from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from djmoney.contrib.exchange.models import convert_money
from djmoney.money import Money

from wallet.forms import WalletForm
from wallet.models import Wallet


class WalletDetail(PermissionRequiredMixin, FormMixin, DetailView):
    model = Wallet
    form_class = WalletForm
    # template_name = 'wallet/wallet_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):
        return self.get_object().user == self.request.user


class WalletList(ListView):
    model = Wallet

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.wallets.all()


class WalletUpdate(PermissionRequiredMixin, UpdateView):

    model = Wallet
    fields = ["name", "profile_pic", "default_currency"]

    def get_success_url(self):
        return reverse("wallet_detail", args=[self.object.id])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):
        return self.get_object().user == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # breakpoint()
        new_curr = request.POST.get("default_currency") or self.object.default_currency
        new_bal = convert_money(
            Money(self.object.balance, self.object.default_currency), new_curr
        )

        self.object.balance = new_bal.amount
        self.object.save()

        return super().post(request, *args, **kwargs)
