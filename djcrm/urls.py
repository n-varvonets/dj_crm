from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page, LandingPageView
# from leads.views import home_page, second_page  # 1)it's already unnecessary because we use url in certain app

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home_page/', home_page), # 2)and after adding url in MY APP
    # path('second_page/', second_page),

    # 3)it necessary to indicate root.. for example with subdomains ____:8000/leads/all with include func...
    path('leads/', include("leads.urls", namespace="leads")),  # namespace - уникальный индетификатор урлов внутри нашего уникального проекта

    # path('', landing_page, name="landing-page")
    path('', LandingPageView.as_view(), name="landing-page")
]
