from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from agents.mixins import OrganiserAndLoginRequiredMixin
# Create your views here.


"""CRUD+L - Create, Retrieve, Update and Delete + List 
this all actions which u can categorized any website... django.views.generic - has all of CRUD """


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        # return "/leads" - this is hard coding... instead of that we can use dynamically by func of reverse for namespace of URL
        return reverse("login")


# def landing_page(request):
#     return render(request, "landing.html")


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def lead_list(request):
    # 2) с помощью  queryset  получаем наши обьекты из модели Lead и передаеим в конткест
    # leads = Lead.objects.all()
    # 1)можно третьим параметром передавать в темплейты контекст(наши переменные)  и потом во вьюхах их принимать {{_}}
    # context = {
    #     "leads": leads
    #     # "object_list": leads >>> it's works for  jango.views.generic LIST
    # }
    # return render(request, "leads/lead_list.html", context)

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    # queryset = Lead.objects.all()  # getting all list of records(leads).... also by default in context passed object_list!!!! not leads!!!

    # context_object_name = "leads"  >>> but also we can indicate name of variable

    def get_queryset(self):
        user = self.request.user  # 1) take our logged in user

        """initial queryset for entire organization"""
        if user.is_organizer:  # 2) if user is organizer so we filtered the leads by his profile(his organization)
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:  # 3) then the user should be an agent
            queryset = Lead.objects.filter(organization=user.agent.organization)  # 4) take all organiztions from agent model for all agents
            """filter"""
            queryset = queryset.filter(agent_user=user)  # 5) take certain organizations by logged user
        return queryset



# pk - это уникальный айди записи в таблице, по кторому мы можем достучаться к конкретной записи
# полученный от от urls.py  и лаьше передавши его templates html
# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead,
#         # "pk": pk  - it's unnecessary to pass pk into the form because pk settle into the lead {{ lead.pk }}
#     }
#     return render(request, "leads/lead_detail.html", context)


class LeadDetailView(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent_user=user)
        return queryset


# def lead_create(request):
#     """create form page with LeadModelForm with fields relation of O2M(Agent), M2M and using save() func. Just compared with  regular Form"""
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             """Django ModelForm allows to save this form"""
#             form.save()  # instead standart Form
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


class LeadCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    # we have to pass the form that we want to work with
    form_class = LeadModelForm

    def get_success_url(self):
        # return "/leads" - this is hard coding... instead of that we can use dynamically by func of reverse for namespace of URL
        return reverse("leads:lead-list")

    def form_valid(self, form):
        """then form is valid and post request is recieved so we can send email about it to some mail"""
        send_mail(
            subject="Theme of message:'The lead was created'",
            message="The main area of message:'Got to the site to see the new lead'",
            from_email="test-mail@test.com",
            recipient_list=["jiyimek160@6ekk.com"]
        )  # http://i.imgur.com/LLu19AL.png - if it shows - need to setup our credentials in setting.py(http://i.imgur.com/i1HlgVc.png)

        return super(LeadCreateView, self).form_valid(form)  # вызываем родительский метод form_valid что бы проверить на корректность данных в форме


# def lead_update(request, pk):
#     """also works with all existing fields including relation O2M, M2M"""
#     lead = Lead.objects.get(id=pk)  # grab the specific lead
#     form = LeadModelForm(instance=lead)  # при новом посте(апдейте) внутрь передаем нашу уже созданную запись,которую хотим обновить
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()  # instead standart Form
#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)


class LeadUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    # queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)  # grab the specific lead
#     lead.delete()
#     return redirect("/leads")

class LeadDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    # queryset = Lead.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)
    
    def get_success_url(self):
        return reverse("leads:lead-list")


"""two extended ways to do CRUD funcs proceed """
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)  # grab the specific lead
#     form = LeadForm()  # при новом посте создаем новый его инстанс
#     if request.method == "POST":
#         """if true than we post data into the form"""
#         form = LeadForm(request.POST)  # >>> <tr><th><label for="id_first_name">First name:</label></th><td><input type="text" name="first_name" value="21"
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             """instead the creating a new lead we use update"""
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.agent = agent
#             lead.save()  # it necessary to commit changes/ or to save them to DB
#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form":form
#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_create(request):
#     form = LeadForm()  # при новом посте создаем новый его инстанс
#     # print(request.POST)  # <QueryDict: {'csrfmiddlewaretoken': ['D98dwOAYBGvMEkoOsedEU9jyZuFtpBiUdweNJ3sf7rQbUVrE4r9SOcTHyLrsWQKu'], 'first_name': ['First Name'], 'last_name': ['Last Name'], 'age': ['213']}>
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadForm(request.POST)
#         # print('form is ..', form)  >>> <tr><th><label for="id_first_name">First name:</label></th><td><input type="text" name="first_name" value="21"
#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)  #{'first_name': 'form name', 'last_name': 'form l_name', 'age': 87}
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()  #  для примера возьмем первого агента(requiered field для создания лида)
#
#             # собсна и создает его...
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print('The lead has been created')
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


