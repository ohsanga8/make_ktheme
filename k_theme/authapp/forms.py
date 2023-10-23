from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Your Username")
    password = forms.CharField(label="Your Password", widget=forms.PasswordInput)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Your Username")
    password = forms.CharField(label="Your Password", widget=forms.PasswordInput)
