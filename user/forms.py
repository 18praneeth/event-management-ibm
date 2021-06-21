from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RangeRequestForm(forms.Form):
    start = forms.DateField(label="Start Date")
    end = forms.DateField(label="End Date")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']