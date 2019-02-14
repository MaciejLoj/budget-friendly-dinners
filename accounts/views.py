from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user) # logs you in after signing up
            # messages.success(request, 'Account created successfully')
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('recipes:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/register.html',{'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recipes:list')
