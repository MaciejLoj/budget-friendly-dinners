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
