web: python manage.py migrate && gunicorn ajedrez.wsgi
release: celery -A ajedrez worker -l info
/* web: sh railway.sh */