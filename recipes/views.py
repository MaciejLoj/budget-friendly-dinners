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

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Przekąski', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganAppetizersFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Przekąski', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatAppetizersView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Przekąski')
    template_name = 'recipes/recipes_base_template.html'


class MeatAppetizersFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Przekąski', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatAppetizersTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Przekąski', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatAppetizersFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Przekąski', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDinnersView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Obiady')
    template_name = 'recipes/recipes_base_template.html'


class VeganDinnersFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Obiady', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDinnersTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Obiady', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDinnersFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Obiady', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDinnersView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Obiady')
    template_name = 'recipes/recipes_base_template.html'


class MeatDinnersFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Obiady', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDinnersTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Obiady', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDinnersFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Obiady', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDessertsView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Desery')
    template_name = 'recipes/recipes_base_template.html'


class VeganDessertsFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Desery', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDessertsTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Desery', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class VeganDessertsFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='WEGE', meal_type='Desery', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDessertsView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Desery')
    template_name = 'recipes/recipes_base_template.html'


class MeatDessertsFiveView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Desery', price='do 5 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDessertsTenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Desery', price='do 10 PLN')
    template_name = 'recipes/recipes_base_template.html'


class MeatDessertsFifteenView(ListView):

    model = Recipe
    context_object_name = 'sorted_recipes'
    queryset = Recipe.objects.filter(typ='MIESO', meal_type='Desery', price='do 15 PLN')
    template_name = 'recipes/recipes_base_template.html'


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
