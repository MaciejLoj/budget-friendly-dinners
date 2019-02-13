from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/register.html',{'form': form})


    # if request.method == 'POST':
    #     f = UserCreationForm(request.POST)
    #     if f.is_valid():
    #         f.save()
    #         messages.success(request, 'Account created successfully')
    #         return redirect('register')
    #
    # else:
    #     f = UserCreationForm()
    #
    # return render(request, 'accounts/register.html', {'form': f})