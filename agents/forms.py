from django import forms
# from leads.models import Agent  # instead indicate the model with which we wanna work with we can extract the certain model by get_user_model
from django.contrib.auth import get_user_model  # Return the User model that is active in this project.
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class AgentModelForm(forms.ModelForm):
    class Meta:
        # model = Agent
        model = User
        # fields = (
        #     'user',
        # )
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )