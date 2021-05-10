#!/bin/bash

python manage.py collectstatic --no-input
python manage.py migrate
# collect static files
gunicorn --worker-class gevent -w 4 -b "0.0.0.0:8000" currency_exchange_app.wsgi --log-level DEBUG
