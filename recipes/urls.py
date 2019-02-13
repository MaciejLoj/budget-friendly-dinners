

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name ='recipes'

urlpatterns = [
    path('', views.new_recipes, name='list'),
    path('dodaj-przepis/', views.create_recipe, name='create'),
    path('do-5-zl/', views.five_zlotys_dinners, name=''),
    path('do-10-zl/', views.ten_zlotys_dinners, name=''),
    path('do-20-zl/', views.twenty_zlotys_dinners, name=''),
    url(r'^(?P<slug>[\w]-]+)/$', views.recipe_detail, name='detail'),
    # zmienna slug zostaje wyslana do views.py jako argument

]