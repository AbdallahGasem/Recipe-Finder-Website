# Generated by Django 5.0.6 on 2024-06-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0028_favrecipes_course_name_alter_recipe_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favrecipes',
            name='course_name',
            field=models.CharField(max_length=255),
        ),
    ]
