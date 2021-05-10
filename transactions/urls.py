from django.urls import path

from transactions.views import TransactionCreate

urlpatterns = [
    path("<wallet_id>/new", TransactionCreate.as_view(), name="new_transaction"),
]
