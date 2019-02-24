from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user) # logs you in after signing up
            # next to name z login.html
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            # przenosi nas .get do naszego next, ktory wzielismy z urla  login.html
            return redirect('recipes:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            save_it = form.save()
            save_it.save()
            subject = 'Potwierdzenie rejestracji!'
            message = ' Dzieki za rejestracje !'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email,settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            #messages.success(request,'Dziekujemy za rejestracje!')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recipes:list')
            # return redirect(request, 'thank_you.html') thank you for registration, please check email
    else:
        form = SignUpForm()
    return render(request,'accounts/register.html',{'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recipes:list')
