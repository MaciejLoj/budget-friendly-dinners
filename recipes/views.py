from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from .forms import CreateRecipe


class FiveZlotysRecipesView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class TenZlotysRecipesView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class FifteenZlotysRecipesView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganRecipesView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE')
    template_name = 'recipes/recipes_base_template.html'


class VeganFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatRecipesView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO')
    template_name = 'recipes/recipes_base_template.html'


class MeatFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganAppetizersView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Przekąski')
    template_name = 'recipes/recipes_base_template.html'


class VeganAppetizersFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Przekąski', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'
    

class VeganAppetizersTenView(ListView):




class VeganAppetizersFifteenView(ListView):




class RecipeDetail(DetailView):

    model = Recipe

    def get(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.all()
        return context


class NewRecipes(ListView):

    model = Recipe
    context_object_name = 'recipes'
    queryset = Recipe.objects.all().order_by('date')
    template_name = 'recipes/all_recipes.html'


@method_decorator(login_required, name='dispatch')
class CreateRecipeView(View):
    form_class = CreateRecipe
    template_name = 'recipes/create_recipe.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('/przepisy')
        return render(request, self.template_name, {'form': form})