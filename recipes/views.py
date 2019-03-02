from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView


class FiveZlotysDinners(View):

    def get(self, request):
        pass


class TenZlotysDinners(View):

    def get(self, request):
        pass


class TwentyZlotysDinners(View):

    def get(self, request):
        pass


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
    template_name = 'recipes/new_recipes.html'



@method_decorator(login_required, name='dispatch')
class ProtectedView(View):
    template_name = 'recipes/create_recipe.html'




    # @login_required(login_url="/uzytkownicy/logowanie/")
    # def create_recipe(request):
    #     if request.method == 'POST':
    #         form = forms.CreateRecipe(request.POST,request.FILES)
    #         if form.is_valid():
    #             instance = form.save(commit=False)
    #             instance.author = request.user
    #             instance.save()
    #             return redirect('recipes:list')
    #     else:
    #         form = forms.CreateRecipe()
    #     return render(request, 'recipes/create_recipe.html', {'form':form})

