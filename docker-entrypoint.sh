#!/bin/bash

python manage.py collectstatic --no-input
python manage.py migrate
# collect static files
gunicorn --worker-class gevent -w 4 -b "0.0.0.0:8000" whistle.wsgi --log-level DEBUG
