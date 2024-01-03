from django.db import models

# Create your models here.

class Recipe(models.Model):
  recipe_name= models.CharField(max_length=30)
  ingredients= models.CharField(max_length=350, help_text='Ingredients must be separated by commas.')
  description= models.TextField()
  cooking_time= models.FloatField(help_text='In minutes')
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  
  # calculate difficulty of recipe using cooking time and number of ingredients
  def calculate_difficulty(self):
    ingredients = self.ingredients.split(', ')
    if self.cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif self.cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif self.cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    elif self.cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = 'Hard'
    return difficulty

  def __str__(self):
    return str(self.recipe_name)