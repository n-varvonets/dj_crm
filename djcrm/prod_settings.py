from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gmsadasdfv411^_hsgfhgfsxcvnx^@r%y@2wqzi^9z@mud+9n'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# указывем путь к моим созданным статическим файлам
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# так же необходимо указать путь ко всем статическим файлам, которые должны быть расположены в одном месте
STATIC_ROOT = "static_root"


