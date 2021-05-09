from moneyed import CURRENCIES


def list_currency_choices():
    list_currency_keys = [(key, key) for key, val in CURRENCIES.items()]
    return list_currency_keys
