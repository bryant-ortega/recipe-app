from django.urls import path
from .views import home
from .views import RecipesListView
from .views import RecipeDetailView

app_name = 'recipes'

urlpatterns = [
   path('', home),
   path("recipes/", RecipesListView.as_view(), name="recipes_list"),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]