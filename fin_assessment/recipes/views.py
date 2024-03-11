from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeCategory, Category
from random import choice


def home(request):
    test = "HOME TEST"
    return render(request, 'recipes/home.html', context={'test': test})


def add_recipe(request):
    test = "ADD RECIPE TEST"
    return render(request, 'recipes/add_recipe.html', context={'test': test})


def login(request):
    test = "LOGIN TEST"
    return render(request, 'recipes/login.html', context={'test': test})


def logout(request):
    test = "LOGOUT TEST"
    return render(request, 'recipes/logout.html', context={'test': test})


def recipe_detail(request):
    test = "recipe_detail TEST"
    return render(request, 'recipes/recipe_detail.html', context={'test': test})


def registration(request):
    test = "REGISTRATION TEST"
    return render(request, 'recipes/registration.html', context={'test': test})
