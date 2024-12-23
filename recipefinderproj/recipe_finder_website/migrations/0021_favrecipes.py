# Generated by Django 5.0.6 on 2024-06-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0020_delete_favrecipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('recipeID', models.IntegerField()),
                ('recipe_NAME', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('userID', 'recipeID')},
            },
        ),
    ]
