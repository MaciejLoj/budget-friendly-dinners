from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.views.generic import RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SignUpView(View):
    template_name = 'accounts/register.html'

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            save_it = form.save()
            save_it.save()
            subject = 'Potwierdzenie rejestracji!'
            message = ' Dzieki za rejestracje !'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list,
                      fail_silently=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recipes:list')

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AddUserView(View):
    template_name = 'add_user.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class UserInfo(View):
    template_name = 'accounts/user_info.html'

    def get(self, request):
        return render(request, self.template_name)
