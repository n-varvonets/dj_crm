from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
# Create your views here.


"""CRUD+L - Create, Retrieve, Update and Delete + List 
this all actions which u can categorized any website... django.views.generic - has all of CRUD """


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()  # getting all list of records(leads).... also by default in context passed object_list!!!! not leads!!!
    # context_object_name = "leads"  >>> but also we can indicate name of variable


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    # we have to pass the form that we want to work with
    form_class = LeadModelForm

    def get_success_url(self):
        # return "/leads" - this is hard coding... instead of that we can use dynamically by func of reverse for namespace of URL
        return reverse("leads:lead-list")


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")





