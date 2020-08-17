web: gunicorn wegemoc.wsgi:application
worker: celery -A wegemoc worker -l info
worker: celery flower -A wegemoc