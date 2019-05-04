
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

    path('z-miesem/przekaski', views.MeatAppetizersView.as_view(), name='meat-appetizers'),
    path('z-miesem/przekaski/do-5-zl/', views.MeatAppetizersFiveView.as_view(), name='meat-appetizers-five'),
    path('z-miesem/przekaski/do-10-zl/', views.MeatAppetizersTenView.as_view(), name='meat-appetizers-ten'),
    path('z-miesem/przekaski/do-15-zl/', views.MeatAppetizersFifteenView.as_view(), name='meat-appetizers-fifteen'),

    path('wege/obiady', views.VeganDinnersView.as_view(), name='vegan-dinners'),
    path('wege/obiady/do-5-zl/', views.VeganDinnersFiveView.as_view(), name='vegan-dinners-five'),
    path('wege/obiady/do-10-zl/', views.VeganDinnersTenView.as_view(), name='vegan-dinners-ten'),
    path('wege/obiady/do-15-zl/', views.VeganDinnersFifteenView.as_view(), name='vegan-dinners-fifteen'),

    path('z-miesem/obiady', views.MeatDinnersView.as_view(), name='meat-dinners'),
    path('z-miesem/obiady/do-5-zl/', views.MeatDinnersFiveView.as_view(), name='meat-dinners-five'),
    path('z-miesem/obiady/do-10-zl/', views.MeatDinnersTenView.as_view(), name='meat-dinners-ten'),
    path('z-miesem/obiady/do-15-zl/', views.MeatDinnersFifteenView.as_view(), name='meat-dinners-fifteen'),

    path('wege/desery', views.VeganDessertsView.as_view(), name='vegan-desserts'),
    path('wege/desery/do-5-zl/', views.VeganDessertsFiveView.as_view(), name='vegan-desserts-five'),
    path('wege/desery/do-10-zl/', views.VeganDessertsTenView.as_view(), name='vegan-desserts-ten'),
    path('wege/desery/do-15-zl/', views.VeganDessertsFifteenView.as_view(), name='vegan-desserts-fifteen'),

    path('z-miesem/desery', views.MeatDessertsView.as_view(), name='meat-desserts'),
    path('z-miesem/desery/do-5-zl/', views.MeatDessertsFiveView.as_view(), name='meat-desserts-five'),
    path('z-miesem/desery/do-10-zl/', views.MeatDessertsTenView.as_view(), name='meat-desserts-ten'),
    path('z-miesem/desery/do-15-zl/', views.MeatDessertsFifteenView.as_view(), name='meat-desserts-fifteen'),

    url(r'^(?P<slug>[\w]-]+)/$', views.RecipeDetail.as_view(), name='detail'),

]
