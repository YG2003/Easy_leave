from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateApplication(forms.Form):
    title = forms.CharField(label = "Title", max_length = 30)
    description = forms.CharField(label = "Description", widget = forms.Textarea(attrs={'rows':5, 'cols': 100}))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    