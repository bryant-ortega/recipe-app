from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe  # to access Recipe model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
from .utils import get_chart

import pandas as pd

# Create your views here.

class RecipesListView(LoginRequiredMixin, ListView):           #class-based "protected" view
   model = Recipe                        
   template_name = 'recipes/recipes_list.html'    

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

def home(request):
  return render(request, 'recipes/recipes_home.html')

#define function-based view - records()
#keep protected
@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    chart = None
    recipes_df_html = None

    if request.method == 'POST' and form.is_valid():
        recipe_name = form.cleaned_data.get('recipe_name')
        category = form.cleaned_data.get('category')
        chart_type = form.cleaned_data.get('chart_type')

        # Building the queryset based on form input
        qs = Recipe.objects.all()
        if recipe_name:
            qs = qs.filter(recipe_name__icontains=recipe_name)
        if category and category != 'Choose':
            qs = qs.filter(category=category)

        # Convert queryset to DataFrame
        if qs.exists():
          recipes_df = pd.DataFrame(list(qs.values('id', 'recipe_name', 'category', 'date_added', 'cooking_time')))
          recipes_df['chart_recipe_name'] = recipes_df['recipe_name']  # Add a new column for chart labels
          recipes_df['recipe_name'] = recipes_df.apply(lambda row: f'<a href="{reverse("recipes:detail", kwargs={"pk": row["id"]})}">{row["recipe_name"]}</a>', axis=1)
          recipes_df_html = recipes_df.to_html(escape=False)

        # Ensure the DataFrame is not empty before generating the chart
        if not recipes_df.empty:
          chart = get_chart(chart_type, recipes_df)
        else:
          # Handle the case where the DataFrame is empty
          # e.g., set chart and recipes_df_html to None or appropriate default values
          pass

    context = {
        'form': form,
        'recipes_df': recipes_df_html,
        'chart': chart
    }

    return render(request, 'recipes/records.html', context)