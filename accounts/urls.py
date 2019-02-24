

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('logowanie/',views.login_view, name='login'),
    path('rejestracja/', views.register, name='register'),
    path('wylogowanie/', views.logout_view, name='logout'),
    path('password_reset/',auth_views.PasswordResetView,name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView, name='password_reset_complete')
]
