from django.utils.module_loading import import_string
from djmoney import settings

from currency_exchange_app.celery import app


@app.task(bind=True)
def update_exchange_rates(self, backend=settings.EXCHANGE_BACKEND, **kwargs):
    backend = import_string(backend)()
    backend.update_rates(**kwargs)
