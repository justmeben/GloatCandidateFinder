#!/bin/bash

echo "Installing dependancies and netcat to make a loop that saves few seconds takes too long, so we just sleep 5 secs"
sleep 5

python manage.py collectstatic
python manage.py migrate
python manage.py init_sample_data
python manage.py create_default_user
gunicorn gloatapp.wsgi:application -w 2 --timeout 300 --access-logfile - --error-logfile - --bind 0.0.0.0:80