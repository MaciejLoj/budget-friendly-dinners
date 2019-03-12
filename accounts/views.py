from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

class SignUpView(View):
    template_name = 'accounts/register.html'

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
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
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UserInfo(View):
    template_name = 'accounts/user_info.html'

    def get(self, request):
        return render(request, self.template_name)


class PasswordChangeView(View):

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
        return render(request,'registration/password_change_form.html', {'form': form, 'message': message})

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request,'registration/password_change_form.html', {'form': form})