from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.


def home_page(request):
    # 2) с помощью  queryset  получаем наши обьекты из модели Lead и передаеим в конткест

    leads = Lead.objects.all()
    # 1)можно третьим параметром передавать в темплейты контекст(наши переменные)  и потом во вьюхах их принимать {{_}}
    context = {
        "leads": leads
    }
    return render(request, "leads/home_page.html", context)


def second_page(request):
    # return HttpResponse("Hello world")
    return render(request, "second_page.html")