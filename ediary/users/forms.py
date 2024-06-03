from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password")