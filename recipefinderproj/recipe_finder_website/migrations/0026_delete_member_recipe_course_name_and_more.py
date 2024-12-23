# Generated by Django 5.0.6 on 2024-06-24 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0025_favrecipes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='recipe',
            name='course_name',
            field=models.CharField(default='main course', max_length=255),
        ),
        migrations.AlterField(
            model_name='favrecipes',
            name='recipeID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_website.recipe'),
        ),
        migrations.AlterField(
            model_name='favrecipes',
            name='userID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_website.user'),
        ),
    ]
