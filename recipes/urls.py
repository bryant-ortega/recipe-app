from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, records
from .views import RecipesListView
from .views import RecipeDetailView


app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path("recipes/", RecipesListView.as_view(), name="recipes_list"),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('recipes/search/', records, name='recipe_search')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)