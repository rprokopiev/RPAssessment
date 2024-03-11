from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeCategory, Category


def index(request):
    message = 'Welcome to ShopApp'
    return render(request, 'recipes/index.html', context={'content': message})
