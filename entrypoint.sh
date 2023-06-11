poetry run python manage.py migrate
exec poetry run gunicorn -w 4 --bind 0.0.0.0:8000 content_management_system.wsgi:application