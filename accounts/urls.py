

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    path('logowanie/',views.login, name='login'),
    path('rejestracja/', views.register, name='signup')


]
