# we can add our script of url for MY CERTAIN APP
# it's useful for project where a lot of services and apps
# by default using from main apps(djcrm) urls which indicated in setting

from django.urls import path
from .views import *

app_name = "leads"

"""this is hardocoding not using URL namespace.. and if I decide to change the url - it also necessary to change in ALL PLACES in templates whenewere I were referenced at them"""
# urlpatterns = [
#     path('', lead_list),
#     path('<int:pk>/', lead_detail),  # pk - это уникальный айди записи в таблице, по кторому мы можем достучаться к конкретной записи
#     path('<int:pk>/update/', lead_update),
#     path('<int:pk>/delete/', lead_delete),
#     path('create/', lead_create),
# ]

urlpatterns = [
    # path('', lead_list, name='lead-list'),
    path('', LeadListView.as_view(), name='lead-list'),
    # path('<int:pk>/', lead_detail, name='lead-detail'),  # pk - это уникальный айди записи в таблиц е, по кторому мы можем достучаться к конкретной записи
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),  # pk - это уникальный айди записи в таблице, по кторому мы можем достучаться к конкретной записи
    # path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    # path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    # path('create/', lead_create, name='lead-create'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),

    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),

]
