from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def five_zlotys_dinners(request):
    pass
    #all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    #return render(request, 'recipes/five_zlotys.html',#'recipes':all_recipes)

def ten_zlotys_dinners(request):
    pass
    # all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    #return render(request, 'recipes/ten_zlotys.html',#'recipes':all_recipes)

def twenty_zlotys_dinners(request):
    pass
    # all_recipes = Recipes.objects.all() pokaze wszystkie za ta cene
    #return render(request, 'recipes/twenty_zlotys.html',#'recipes':all_recipes )

def recipe_detail(request,slug):
    # will find a recipe in the database by slug, our given argument()
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})

def new_recipes(request):
    new = Recipe.objects.all().order_by('date') # nazwa z modeli
    return render(request, 'recipes/new_recipes.html',{'recipes': new})