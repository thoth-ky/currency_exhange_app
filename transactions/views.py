from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from transactions.forms import TransactionForm
from transactions.models import Transaction


class TransactionCreate(FormView):
    template_name = "transactions/transactions_form.html"
    form_class = TransactionForm

    def get_success_url(self):
        return reverse("wallet_detail", args=[self.kwargs["wallet_id"]])

    def form_valid(self, form):
        transaction_record = Transaction(
            source_wallet_id=self.kwargs["wallet_id"], **form.cleaned_data
        )
        transaction_record.save()

        return super(TransactionCreate, self).form_valid(form)
