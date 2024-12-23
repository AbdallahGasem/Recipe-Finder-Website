from django.urls import path
from . import views

urlpatterns = [
    #Registration and Validation#
    path('', views.loginTemplate, name='loginTemplate'),
    path('Authnticate/', views.loginAuthentication, name='loginAuthntication'),
    path('Register/', views.signUpTemplate, name='signUpTemplate'),
    path('add_user/', views.addrecord, name='addrecord'),

    # for admin add recipe button
    path('add_recipe/', views.addRecipeTemplate, name='addRecipeTemplate'),

    #navbar links
    path('userOpeningPage/', views.user_opening_page_view, name='userHome'),
    #path('userOpeningPage/', views.userOpeningPage, name='userHome'),
    path('adminOpeningPage/', views.adminOpeningPage, name='adminHome'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('A_FAQ/', views.adminFAQ, name='adminFAQ'),
    path('U_FAQ/', views.userFAQ, name='userFAQ'),

    #admin CRUD#
    #add recipe
    path('recipe_added', views.addRecipe, name='addRecipe'),

    #delete recipe
    path('recipe_deleted/<int:id>' , views.deleteRecipe, name='deleteRecipe'),

    #load edit recipe template
    path('edit_recipe/<int:id>' , views.editRecipeTemplate, name='editRecipeTemplate'),
    #edit recipe
    path('recipe_edited/<int:id>' , views.editRecipe, name='editRecipe'),

    #display recipe when img clicked
    path('display_recipe/<int:id>' , views.dispalyRecipe, name='displayRecipe'),
    #show favourites
    path('add_to_fav/<int:recipe_id>/', views.add_to_fav, name='add_to_fav'),

    path('show_favs/',views.show_favs,name='show_favs'),

    path('delete_fav_Recipe/<int:id>/',views.delete_fav_Recipe,name='delete_fav_Recipe'),

    # path('add/', views.add_new_user, name='add_new_user'),
    # path('login/add/', views.add_new_user, name='add_new_user'),
    # path('addrecord/', views.addrecord, name='addrecord'),
    # path('add/addrecord/', views.addrecord, name='addrecord'),
    # path('deleterecord/<int:id>', views.deleterecord, name='deleterecord'),
    # path('login/', views.login, name='login'),
    # path('recipe_finder_website/members', views.members, name='members'),
]