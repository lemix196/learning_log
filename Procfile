web: gunicorn learning_log.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate