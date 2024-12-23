# Generated by Django 5.0.6 on 2024-06-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_website', '0006_remove_user_confpass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=255)),
                ('instructions', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='RecipePhotos')),
            ],
        ),
    ]
