#!/bin/bash
echo "Starting Hereoku exec"
/bin/bash ./.profile.d/heroku-exec.sh

echo "Finalized Hereoku exec"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

# collect static files
# python manage.py createsuperuser --username admin --noinput
echo "Starting Supervisor"
supervisord -c supervisord.conf
supervisorctl -c supervisord.conf status all
echo "Done.Start Gunicorn"
gunicorn currency_exchange_app.wsgi --log-file -
