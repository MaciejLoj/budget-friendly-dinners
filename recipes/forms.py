from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateRecipe(forms.ModelForm):

    class Meta:
        model = models.Recipe
        fields = ['title','body','slug','image']

# customuserform z mailem loginem, passwordem

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Wymagane pole.')

    class Meta:
        model = User
        fields = ['username','password1','password2','email']