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

class UserDetailsForm(forms.Form):
    first_name = forms.CharField(label = "First Name", max_length = 50)
    last_name = forms.CharField(label = "Last Name", max_length = 30)
    phone = forms.CharField(label = "Mobile Number", max_length = 10)
    email = forms.EmailField(label = "Email Address")
    address = forms.CharField(label = "Permanent Address", widget = forms.Textarea(attrs={'rows':5, 'cols': 100}))
    