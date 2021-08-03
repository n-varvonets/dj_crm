from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm
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


def lead_create(request):
    form = LeadForm()  # при новом посте создаем новый его инстанс
    # print(request.POST)  # <QueryDict: {'csrfmiddlewaretoken': ['D98dwOAYBGvMEkoOsedEU9jyZuFtpBiUdweNJ3sf7rQbUVrE4r9SOcTHyLrsWQKu'], 'first_name': ['First Name'], 'last_name': ['Last Name'], 'age': ['213']}>
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadForm(request.POST)
        # print('form is ..', form)  >>> <tr><th><label for="id_first_name">First name:</label></th><td><input type="text" name="first_name" value="21"
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)  #{'first_name': 'form name', 'last_name': 'form l_name', 'age': 87}
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()  #  для примера возьмем первого агента(requiered field для создания лида)

            # собсна и создает его...
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print('The lead has been created')
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

