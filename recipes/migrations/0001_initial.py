# Generated by Django 4.2.6 on 2024-01-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=30)),
                ('ingredients', models.CharField(help_text='Ingredients must be separated by commas.', max_length=350)),
                ('description', models.TextField()),
                ('cooking_time', models.FloatField(help_text='In minutes')),
            ],
        ),
    ]