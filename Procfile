release: python manage.py migrate
web: gunicorn english.wsgi --log-file=-
worker: celery --app english worker -l info