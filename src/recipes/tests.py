from django.test import TestCase
from .models import Recipe      #to access Recipe model

# Create your tests here.
class RecipeModelTest(TestCase):

  def setUpTestData():
    # Set up non-modified objects used by all test methods
    Recipe.objects.create(recipe_name='Lemonade', ingredients='water, lemon juice, honey', description= 'Add lemon juice to water and add honey', cooking_time=5)

  def test_recipe_name(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'recipe_name' field and use it to query its data
    recipe_name_label = recipe._meta.get_field('recipe_name').verbose_name

    # Compare the value to the expected result
    self.assertEqual(recipe_name_label, 'recipe name')

  def test_ingredients(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 350)

  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    recipe_name_max_length = recipe._meta.get_field('recipe_name').max_length
    self.assertEqual(recipe_name_max_length, 30)

  def test_difficulty_calcuation(self):
    # Testing the calculate_difficulty function
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.calculate_difficulty(), 'Easy')