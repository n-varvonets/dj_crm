from django import forms


class LeadForm(forms.Form):
    """inpute inside the fields which has to recieve the forms"""
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)