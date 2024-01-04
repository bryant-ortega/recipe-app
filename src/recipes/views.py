from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access Recipe model

# Create your views here.

class RecipesListView(ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipes/recipes_list.html'    #specify template 

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

def home(request):
  return render(request, 'recipes/recipes_home.html')

