"""
Django settings for djcrm project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ


env = environ.Env(
    #
    DEBUG=(bool, False)
)
# Но в проде мы его не будем использовать, по тому что .env не хранится в репозитории(желтым цветом для гита).
# мы его используем локально для чтения наших переменных  DEBUG and SECRET_KEY  в фйале djcrm/.env
# мы даже его можем сейчас закоментить(упадет ошибка http://i.imgur.com/Ny5lyhD.png), но если для нашей сессии мы эти
# значения(с файла djcrm/.env) заэкспортируем в консоле, то сервер запуститься без ошибок
# environ.Env.read_env()
READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE: # по дефолту мы установили это значение - False(что бы команда не читала локально SECRET_KEY in djcrm/.env без эскортирования вручную READ_DOT_ENV_FILE=True)
    """ и если кто-то вручную в консоле прописал export READ_DOT_ENV_FILE=True,
     то тогда читаем SECRET_KEY in djcrm/.env  lkz pfgecrf l;fyub"""
    environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# print(DEBUG, SECRET_KEY)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'crispy_forms',
    'crispy_tailwind',

    # Local apps
    'leads',
    'agents',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djcrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djcrm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# указывем путь к моим созданным статическим файлам
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# так же необходимо указать путь ко всем статическим файлам, которые должны быть расположены в одном месте
STATIC_ROOT = "static_root"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Указываю в какой прилажухе будет мой аутифицированный юзер
AUTH_USER_MODEL = 'leads.User'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #  - that's how to configure email.. + need to adjust smpt
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # but right now I want to send email in console

LOGIN_REDIRECT_URL = '/leads'
LOGIN_URL = '/login'  # need for LoginRequiredMixin... for redirecting from restricted page not authed users to login page.
LOGOUT_REDIRECT_URL = '/'

# for ability to use Crispy  forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'
