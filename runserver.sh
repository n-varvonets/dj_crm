python manage.py collectstatic --no-input

python manage.py migrate

gunicorn --worker-tmp-dir /dev/shm djcrm.wsgi  # gunicorn djcrm.wsgi:application -  this is the same as "python manage.py runserver" - but that's how run the app in production of DigitalOcean

# chmod +x runserver.sh
# ./runserver.sh