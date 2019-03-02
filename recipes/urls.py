

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.NewRecipes.as_view(), name='list'),
    path('dodaj-przepis/', views.ProtectedView.as_view(), name='create'),
    path('do-5-zl/', views.FiveZlotysDinners.as_view(), name='tofive'),
    path('do-10-zl/', views.TenZlotysDinners.as_view(), name='toten'),
    path('do-20-zl/', views.TwentyZlotysDinners.as_view(), name='totwenty'),
    url(r'^(?P<slug>[\w]-]+)/$', views.RecipeDetail.as_view(), name='detail'),


]