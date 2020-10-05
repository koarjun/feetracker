web: gunicorn feetracker.wsgi --log-file -
release: python manage.py makemigrations students &&  python manage.py migrate students
