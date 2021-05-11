#!/bin/bash
/bin/bash ./.profile.d/heroku-exec.sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

# collect static files
python manage.py createsuperuser --username admin --noinput
supervisorctl -c supervisord.conf start all
gunicorn currency_exchange_app.wsgi --log-file -
