from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView, SignupView
from django.conf import settings  # import our dirs of static which we specify in setting.py
from django.conf.urls.static import static  # special func from django for indicating  static url and
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include("leads.urls", namespace="leads")),  # namespace - уникальный индетификатор урлов внутри нашего уникального проекта
    path('', LandingPageView.as_view(), name="landing-page"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')

]


"""при деплое нужно указывать статические фалйы для digital oceone space  для управения статич файлов(при посте новых 
и чтении существющих)... т.е. нужно чекнуть если дебаг тру,т.е. на деплое, то указываем путь к нашим статич файлам"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)