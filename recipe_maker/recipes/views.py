from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    return render(request, 'recipes/home.html')

def dishes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/dishes.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_ingredients(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    # Split ingredients by comma
    ingredients_list = [i.strip() for i in recipe.ingredients.split(',')]
    return render(request, 'recipes/ingredients.html', {
        'recipe': recipe,
        'ingredients_list': ingredients_list
    })

# Steps page
def recipe_steps(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    # Split steps by newline
    steps_list = [s.strip() for s in recipe.steps.split('\n') if s.strip()]
    return render(request, 'recipes/steps.html', {
        'recipe': recipe,
        'steps_list': steps_list
    })
