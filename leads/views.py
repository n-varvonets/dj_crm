from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.


def lead_list(request):
    # 2) с помощью  queryset  получаем наши обьекты из модели Lead и передаеим в конткест

    leads = Lead.objects.all()
    # 1)можно третьим параметром передавать в темплейты контекст(наши переменные)  и потом во вьюхах их принимать {{_}}
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


# pk - это уникальный айди записи в таблице, по кторому мы можем достучаться к конкретной записи
# полученный от от urls.py  и лаьше передавши его templates html
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
        "pk": pk
    }
    return render(request, "leads/lead_detail.html", context)