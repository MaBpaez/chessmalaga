#!/bin/bash
python manage.py migrate
gunicorn ajedrez.wsgi
celery -A ajedrez worker -l info