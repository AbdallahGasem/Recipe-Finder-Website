# Generated by Django 5.0.6 on 2024-06-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0008_alter_recipe_ingredients_alter_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/RecipePhotos'),
        ),
    ]
