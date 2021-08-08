from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin
# Create your views here.


class AgentsListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        # return Agent.objects.all()  # instead to return all agents we gonna return all related agents to one lead
        """so filtered agents by they organization(UserProfile)"""
        grab_the_actual_user_who_is_logged_in_the_site = self.request.user  # >>> New - http://i.imgur.com/gRd4djy.png - look at the userprofile
        """and for our model Agent need to set two field on of those is organization from UserProfile(http://i.imgur.com/j4aY2wV.png)"""
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        """что бы не падала ошибка при созданнии агента, то нужно в нее передать организацию(ЮзерПрофайл)"""
        agent = form.save(commit=False)  # берем полученную форму(с юзером,но без организации), НО не сохраняем её в бд
        """у ЗАЛОГИНЕННОГО пользователя по дефолту создаются юезрпрофайл(организация) через signals.
         Достаем его и записываем в модель агента"""
        agent.organization = self.request.user.userprofile
        agent.save()  # а теперь с атрибутом organization можем сохранить только что созданную запись агента
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = 'agent'  # for template to indicate our context

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = 'agent'  # for template to indicate our context

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse("agents:agent-list")