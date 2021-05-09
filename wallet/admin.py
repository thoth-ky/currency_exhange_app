from django.contrib import admin
from django.contrib.auth.decorators import login_required

from wallet.models import Wallet


class WalletAdmin(admin.ModelAdmin):
    pass


admin.site.login = login_required(admin.site.login)
admin.site.register(Wallet, WalletAdmin)
