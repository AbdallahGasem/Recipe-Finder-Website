# Generated by Django 5.0.6 on 2024-06-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0013_rename_recipeid_favrecipes_recipe_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favrecipes',
            name='userID',
            field=models.IntegerField(),
        ),
    ]
