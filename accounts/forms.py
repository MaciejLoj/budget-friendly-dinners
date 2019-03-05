from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=25, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
