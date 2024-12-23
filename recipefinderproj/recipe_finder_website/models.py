from django.db import models
class User (models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255 ,default='example@example.com')
  usertype = models.CharField(max_length=255 , default = 'user')

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    course_name=models.CharField(max_length=255)
    ingredients = models.CharField(max_length=1000)
    instructions = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='RecipePhotos', null=True, blank=True)

class FavRecipes(models.Model):
    userID = models.ForeignKey(User,on_delete = models.CASCADE)
    recipeID = models.ForeignKey(Recipe,on_delete = models.CASCADE)
    course_name = models.CharField(max_length=255)
    recipe_NAME=models.CharField(max_length=255)
    recipe_image = models.ImageField(upload_to='RecipePhotos', null=True, blank=True)