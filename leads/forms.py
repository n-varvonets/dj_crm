from django import forms
from .models import Lead
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
