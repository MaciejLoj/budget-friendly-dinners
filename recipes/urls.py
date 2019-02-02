

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('do-5-zl/', views.five_zlotys_dinners, 'recipes/five_zlotys.html', name=''),
    path('do-10-zl/', views.ten_zlotys_dinners, 'recipes/ten_zlotys.html', name=''),
    path('do-20-zl/', views.twenty_zlotys_dinners, 'recipes/twenty_zlotys.html', name=''),

]