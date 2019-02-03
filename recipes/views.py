from django.shortcuts import render
from django.http import HttpResponse

def five_zlotys_dinners(request):
    #all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    return render(request, 'recipes/five_zlotys.html',#'recipes':all_recipes)

def ten_zlotys_dinners(request):
    # all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    return render(request, 'recipes/ten_zlotys.html',#'recipes':all_recipes)

def twenty_zlotys_dinners(request):
    # all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    return render(request, 'recipes/twenty_zlotys.html',#'recipes':all_recipes )