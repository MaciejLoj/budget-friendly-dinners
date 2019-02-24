from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=25,required=True)

    class Meta:
        model = User
        fields = ['username','password1','password2','email']

"""

class MyForm(forms.Form)
    email
    login
    haslo
    
"""