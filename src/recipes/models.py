from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
  CATEGORY_CHOICES = [
    ('DESSERT', 'Dessert'),
    ('MAIN_COURSE', 'Main Course'),
    ('APPETIZER', 'Appetizer'),
    ('BEVERAGE', 'Beverage'),
  ]
  recipe_name= models.CharField(max_length=30)
  ingredients= models.CharField(max_length=350, help_text='Ingredients must be separated by commas.')
  description= models.TextField()
  cooking_time= models.FloatField(help_text='In minutes')
  category= models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='DESSERT')
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
  date_added = models.DateTimeField(default=timezone.now)

  
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
        difficulty = self.calculate_difficulty()
        return f"id: {self.id}, Name: {self.recipe_name}, Category: {self.category}, Cooking Time: {self.cooking_time} minutes, Difficulty: {difficulty}"

  
  def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})