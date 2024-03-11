from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeCategory, Category
from random import choice


def home(request):
    home_recipes = []
    recipes = Recipe.objects.all()
    for _ in range():
        home_recipes.append()
    return render(request, 'recipes/home.html', context={'content': message})
