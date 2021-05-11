import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_exchange_app.settings")

app = Celery("currency_exchange_app")


app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update_rates": {
        "task": "wallet.tasks.update_exchange_rates",
        "schedule": crontab(),
        "kwargs": {},  # For custom arguments
    }
}
