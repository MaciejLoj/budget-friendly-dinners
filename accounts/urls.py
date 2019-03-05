from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('logowanie/', auth_views.LoginView.as_view(), name='login'),
    path('rejestracja/', views.SignUpView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('zmiana-hasla/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('zmiana-hasla/ok/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('moje_przepisy/', views.UserInfo.as_view(), name='user_info'),
]
