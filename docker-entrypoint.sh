#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
# collect static files
python manage.py createsuperuser --username admin --noinput
gunicorn currency_exchange_app.wsgi --log-file -
