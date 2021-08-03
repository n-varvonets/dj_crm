# we can add our script of url for MY CERTAIN APP
# it's useful for project where a lot of services and apps
# by default using from main apps(djcrm) urls which indicated in setting

from django.urls import path
from .views import home_page, second_page

# уникальный индекфикатор урлдов нашего app, который был получен из djcrm/urls.py
app_name = "leads"

urlpatterns = [
    path('all/', home_page),
    path('', second_page),
]
