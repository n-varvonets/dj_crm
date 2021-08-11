from django import forms
from .models import Lead, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    """if we want to display fields from model including relations O2M, M2M"""
    class Meta:  # in MEta we specify information about the form
        model = Lead
        """ specify the fields which we want to display in actual form from model"""
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )


class LeadForm(forms.Form):
    """inpute inside the fields which has to recieve the forms(standart form without O2M)"""
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    # agent = forms.ChoiceField(choices=(
    #     ('Agent 1', 'Agent 1'),
    #     ('Agent 2', 'Agent 2'),
    # ))

    """1)above it's good example of choice field, but Django provide mach better"""
    # agent = forms.ModelChoiceField(queryset=Agent.objects.none())  # 1/2) it's hard coding to indicate queryset not dynamically
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())  # 2)it's very difficult to dynamically to specify the queryset
    # 3)so we need to overwrite the values of queryset every time the worm is rendering

    # 4)for this we need to overwrite init method. For it we have to pass additional arguments(kwargs) about the user
    # and his agents. In views need to rewrite def get_form_kwargs and passed them here.
    def __init__(self, *args, **kwargs):
        """5)we need to check the request user and based on him we can filter for all agents which belong to this organiztion """
        # print(kwargs)  # 6)>>> {'request': <WSGIRequest: GET '/leads/2/assign-agent/'>}
        request = kwargs.pop("request")  # 7)со всех получаемых аргементов ВЫРЕЗАЕМ наш доп.аргумент(реквест)
        # print(request.user)   # >>> nick
        agents = Agent.objects.filter(organization=request.user.userprofile)  # берем наших всех агентов текущего юзера
        super(AssignAgentForm, self).__init__(*args, **kwargs)  # 8)и передаем его дальше без нашего доп.аргумента("request") как ни в чем и не бывало
        self.fields['agent'].queryset = agents# 9)и меняем установленное в нашем поле его значение. После вызова супер - потому что наше поле 'agent' еще не существует


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "category",
        )





