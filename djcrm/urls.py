from django.contrib import admin
from django.urls import path
from leads.views import home_page, second_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', home_page),
    path('second_page/', second_page),
]
