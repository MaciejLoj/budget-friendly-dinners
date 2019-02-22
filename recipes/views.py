from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms

def five_zlotys_dinners(request):
    pass

def ten_zlotys_dinners(request):
    pass


def twenty_zlotys_dinners(request):
    pass


def recipe_detail(request,slug):
    # will find a recipe in the database by slug, our given argument()
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})

def new_recipes(request):
    new = Recipe.objects.all().order_by('date') # nazwa z modeli
    return render(request, 'recipes/new_recipes.html',{'recipes': new})


@login_required(login_url="/uzytkownicy/logowanie/")
def create_recipe(request):
    if request.method == 'POST':
        form = forms.CreateRecipe(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('recipes:list')
    else:
        form = forms.CreateRecipe()
    return render(request, 'recipes/create_recipe.html', {'form':form})

