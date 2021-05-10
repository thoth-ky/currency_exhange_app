from django.urls import path

from wallet.views import WalletDetail
from wallet.views import WalletList
from wallet.views import WalletUpdate

urlpatterns = [
    path("", WalletList.as_view(), name="wallet_list"),
    path("<pk>", WalletDetail.as_view(), name="wallet_detail"),
    path("<pk>/update", WalletUpdate.as_view(), name="wallet_update"),
]
