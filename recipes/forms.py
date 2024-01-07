from django import forms

CATEGORY_CHOICES = [
  ('DESSERT', 'Dessert'),
  ('MAIN_COURSE', 'Main Course'),
  ('APPETIZER', 'Appetizer'),
  ('BEVERAGE', 'Beverage'),
]

CHART__CHOICES = (        #specify choice as a tuple
  ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)
#define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
  recipe_name= forms.CharField(max_length=30, required=False)
  category= forms.ChoiceField(choices=[('','Choose')] + CATEGORY_CHOICES, required=False)
  chart_type = forms.ChoiceField(choices=CHART__CHOICES)