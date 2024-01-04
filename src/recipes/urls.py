from django.urls import path
from .views import home
from .views import RecipesListView

app_name = 'recipes'

urlpatterns = [
   path('', home),
   path("recipes/", RecipesListView.as_view(), name="recipes_list"),
]