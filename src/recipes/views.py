from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access Recipe model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required

# Create your views here.

class RecipesListView(LoginRequiredMixin, ListView):           #class-based "protected" view
   model = Recipe                         #specify model
   template_name = 'recipes/recipes_list.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

def home(request):
  return render(request, 'recipes/recipes_home.html')

#define function-based view - records(records())
#keep protected
@login_required
def records(request):
   #do nothing, simply display page
   return render(request, 'recipes/records.html')