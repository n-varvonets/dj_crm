from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    # return HttpResponse("Hello world")
    return render(request, "leads/home_page.html")


def second_page(request):
    # return HttpResponse("Hello world")
    return render(request, "second_page.html")