

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.NewRecipes.as_view(), name='list'),
    path('dodaj-przepis/', views.CreateRecipeView.as_view(), name='create'),

    path('do-5-zl/', views.FiveZlotysRecipesView.as_view(), name='to-five'),
    path('do-10-zl/', views.TenZlotysRecipesView.as_view(), name='to-ten'),
    path('do-15-zl/', views.FifteenZlotysRecipesView.as_view(), name='to-fifteen'),

    path('wege/', views.VeganRecipesView.as_view(), name='all-vegan'),
    path('wege/do-5-zl/', views.VeganFiveView.as_view(), name='vegan-five'),
    path('wege/do-10-zl/', views.VeganTenView.as_view(), name='vegan-ten'),
    path('wege/do-15-zl/', views.VeganFifteenView.as_view(), name='vegan-fifteen'),

    path('z-miesem/', views.MeatRecipesView.as_view(), name='all-meat'),
    path('z-miesem/do-5-zl/', views.MeatFiveView.as_view(), name='meat-five'),
    path('z-miesem/do-10-zl/', views.MeatTenView.as_view(), name='meat-ten'),
    path('z-miesem/do-15-zl/', views.MeatFifteenView.as_view(), name='meat-fifteen'),

    path('wege/przekaski', views.VeganAppetizersView.as_view(), name='vegan-appetizers'),
    path('wege/przekaski/do-5-zl/', views.VeganAppetizersFiveView.as_view(), name='vegan-appetizers-five'),
    path('wege/przekaski/do-10-zl/', views.VeganAppetizersTenView.as_view(), name='vegan-appetizers-ten'),
    path('wege/przekaski/do-15-zl/', views.VeganAppetizersFifteenView.as_view(), name='vegan-appetizers-fifteen'),

    # path('z-miesem/przekaski', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/przekaski/do-5-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/przekaski/do-10-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/przekaski/do-15-zl/', views.ProtectedView.as_view(), name=''),
    #
    # path('wege/obiady', views.ProtectedView.as_view(), name=''),
    # path('wege/obiady/do-5-zl/', views.ProtectedView.as_view(), name=''),
    # path('wege/obiady/do-10-zl/', views.ProtectedView.as_view(), name=''),
    # path('wege/obiady/do-15-zl/', views.ProtectedView.as_view(), name=''),
    #
    # path('z-miesem/obiady', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/obiady/do-5-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/obiady/do-10-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/obiady/do-15-zl/', views.ProtectedView.as_view(), name=''),
    #
    # path('wege/desery', views.ProtectedView.as_view(), name=''),
    # path('wege/desery/do-5-zl/', views.ProtectedView.as_view(), name=''),
    # path('wege/desery/do-10-zl/', views.ProtectedView.as_view(), name=''),
    # path('wege/desery/do-15-zl/', views.ProtectedView.as_view(), name=''),
    #
    # path('z-miesem/desery', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/desery/do-5-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/desery/do-10-zl/', views.ProtectedView.as_view(), name=''),
    # path('z-miesem/desery/do-15-zl/', views.ProtectedView.as_view(), name=''),

    url(r'^(?P<slug>[\w]-]+)/$', views.RecipeDetail.as_view(), name='detail'),
]
