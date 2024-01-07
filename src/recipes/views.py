from django.shortcuts import render
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
   model = Recipe                         #specify model
   template_name = 'recipes/recipes_list.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

def home(request):
  return render(request, 'recipes/recipes_home.html')

#define function-based view - records()
#keep protected
@login_required
def records(request):
   #create instance of RecipeSearchForm that you defined in recipes/forms.py
   form = RecipeSearchForm(request.POST or None)
   recipes_df=None     #initialize dataframe to None
   chart = None

   #check if the button is clicked
   if request.method =='POST' and form.is_valid():
      #read recipe_name and chart_type 
      recipe_name = request.POST.get('recipe_name')
      category = form.cleaned_data.get('category')
      chart_type = request.POST.get('chart_type')

      #apply filter to extract data
      qs = Recipe.objects.all()
      if recipe_name:
        qs = qs.filter(recipe_name__icontains=recipe_name)
        #convert the queryset values to pandas dataframe
        recipes_df=pd.DataFrame(qs.values()) 

      # Filter by category if provided and not the default "Choose"
      if category and category != '':
        qs = qs.filter(category=category)

      if qs.exists():
        recipes_df = pd.DataFrame(list(qs.values('recipe_name', 'category', 'date_added', 'cooking_time')))
        chart = get_chart(chart_type, recipes_df)

        #convert the dataframe to html
        recipes_df=recipes_df.to_html()

      #display in terminal - needed for debugging during development only
      print (recipe_name, chart_type)


      print ('Exploring querysets:')
      print ('Case 1: Output of Recipe.objects.all()')
      qs=Recipe.objects.all()
      print (qs)

      print(f"Case 2: Output of Recipe.objects.filter(recipe_name={recipe_name})")
      qs =Recipe.objects.filter(recipe_name=recipe_name)
      print (qs)

      print ('Case 3: Output of qs.values')
      print (qs.values())

      print ('Case 4: Output of qs.values_list()')
      print (qs.values_list())

      print ('Case 5: Output of Recipe.objects.get(id=1)')
      obj = Recipe.objects.get(id=1)
      print (obj)

   #pack up data to be sent to template in the context dictionary
   context={
      'form': form,
      'recipes_df': recipes_df,
      'chart': chart
   }

   #load the recipes/records.html page using the data that you just prepared
   return render(request, 'recipes/records.html', context)