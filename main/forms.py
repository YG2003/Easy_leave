from django import forms
from .models import *

class CreateApplication(forms.Form):
    title = forms.CharField(label = "Title", max_length = 30)
    description = forms.CharField(label = "Description", widget = forms.Textarea(attrs={'rows':5, 'cols': 100}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length = 30, label = "Name")
    password = forms.CharField(max_length = 30, label = "Password")
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone Number")
    status = (
        ('Manager','Manager'),
        ('Worker', 'Worker'),
    )
    position = forms.ChoiceField(choices = status, widget = forms.RadioSelect)


    