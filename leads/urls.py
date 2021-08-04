# we can add our script of url for MY CERTAIN APP
# it's useful for project where a lot of services and apps
# by default using from main apps(djcrm) urls which indicated in setting

from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

# уникальный индекфикатор урлдов нашего app, который был получен из djcrm/urls.py
app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', lead_detail),  # pk - это уникальный айди записи в таблице, по кторому мы можем достучаться к конкретной записи
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),
    path('create/', lead_create),
]
