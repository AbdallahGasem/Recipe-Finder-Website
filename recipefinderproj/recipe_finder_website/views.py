from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import User,Recipe,FavRecipes
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import json

#____________________________________________________REGESTRATION & VALIDATION____________________________________________________#

# شغالة
# name = add_new_user for prev
# load signip template
def signUpTemplate(request):
    return render(request, 'sign_log/SignUp_Page.html')


# شغالة
# add new user to the database using signup form
def addrecord(request):
    if request.method == 'POST':
        Uname = request.POST.get('uname')
        Pass = request.POST.get('password')
        ConfPass = request.POST.get('confpass')
        Email = request.POST.get('mail')
        Type = request.POST.get('option')

        # check user exists in the database
        user = User.objects.filter(email=Email).exists()
        if user == True :
            message = "Email already exists"
            return render(request, 'Sign_log/SignUp_Page.html', {'message': message})
        # check password and confirm password match
        if Pass != ConfPass:
            message = "Password and Confirm Password do not match"
            return render(request, 'Sign_log/SignUp_Page.html', {'message': message})

        # If all validations pass, create the user 

        newuser = User(username = Uname , password = Pass , email = Email , usertype = Type )
        newuser.save()
        # Store user ID in the session
        request.session['user_id'] = int(newuser.id)
        request.session['mail'] = newuser.email
        request.session['pass'] = newuser.password
        if newuser.usertype=='user':
            # return render(request,'USER OPENNING PAGE.html') #reverse to user page instead
            return HttpResponseRedirect(reverse('userHome'))    #line 251 : USERHOME
        elif newuser.usertype=='admin':
            # return render(request,'ADMIN - OPENING PAGE.html')  #reverse to admin page instead
            return HttpResponseRedirect(reverse('adminHome'))





# شغالة
# name = login for prev
# load login template
def loginTemplate(request):
    return render(request, 'sign_log/Login_Page.html')

def loginAuthentication(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('pass')

        try:
            myuser = User.objects.get(email=mail)
        except User.DoesNotExist:
            message = 'Your credentials are incorrect, there is no such user.'
            return render(request, 'Sign_log/Login_Page.html', {'msg': message})

        if myuser:
            if myuser.password == password:
                # Store user ID in the session
                request.session['user_id'] = int(myuser.id)
                request.session['mail'] = myuser.email
                request.session['pass'] = myuser.password

                if myuser.usertype == 'user':
                    return HttpResponseRedirect(reverse('userHome'))
                elif myuser.usertype == 'admin':
                    return HttpResponseRedirect(reverse('adminHome'))
            else:
                message = 'Your credentials are incorrect.'
                return render(request, 'Sign_log/Login_Page.html', {'msg': message})
    else:
        return render(request, 'Sign_log/Login_Page.html')

# شغالة
#add recipe template
def addRecipeTemplate(request):
    return render(request, 'ADMIN-addrecipe.html')

#edited at line 251 to sync with SEARCH#
# def userOpeningPage(request):   # HOME for user
#     context = {'Recipes' :  Recipe.objects.all()}
#     return render(request, 'USER OPENNING PAGE.html' , context)

def adminOpeningPage(request):  # HOME for admin
    context = {'Recipes' : Recipe.objects.all()}
    return render(request, 'ADMIN - OPENING PAGE.html' , context)


#navbar rendering FNs
# def aboutUs(request):  
def aboutUs(request):   #search apply here
    recipes = Recipe.objects.all()
    recipes_list = [{
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'image': recipe.image.url if recipe.image else ''
    } for recipe in recipes]
    qs_json = json.dumps(recipes_list)
    return render(request, 'aboutus.html', {'recipes_list': recipes_list, 'qs_json': qs_json})

def adminFAQ(request):   #for admin
    return render(request, 'adminFAQ.html')

# def userFAQ(request):   #for user
#     return render(request, 'userFAQ.html')
def userFAQ(request):   #search apply here
    recipes = Recipe.objects.all()
    recipes_list = [{
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'image': recipe.image.url if recipe.image else ''
    } for recipe in recipes]
    qs_json = json.dumps(recipes_list)
    return render(request, 'userFAQ.html', {'recipes_list': recipes_list, 'qs_json': qs_json})



#____________________________________________________REICPES ADD/DEL/EDIT_________________________________________________________#
#add recipe to the database with ajax
def addRecipe(request):
    success = ''
    if request.method == 'POST':
        rname = request.POST['recipeName']
        ringredients = request.POST['recipeIngredients']
        rinstructions = request.POST['recipeInstructions']
        rimage = request.FILES['recipeImageFile']  # Use request.FILES to get the uploaded file
        rcourse = request.POST['courses']

        newrecipe = Recipe(name=rname, ingredients=ringredients, instructions=rinstructions, image=rimage,course_name = rcourse)

        if Recipe.objects.filter(name = rname).exists():
            success = rname + " Recipe already exists!"
            return HttpResponse(success)



        else:
            newrecipe.save()
            success = rname + " has been added successfully"
            return HttpResponse(success)

    return HttpResponse('Failed to add recipe')



#delete recipe from the database
def deleteRecipe(request , id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return HttpResponseRedirect(reverse('adminHome'))


#edit recipe template
def editRecipeTemplate(request , id):
    recipe = Recipe.objects.get(id = id)
    context = {'R_edit' : recipe}
    return render(request , 'ADMIN-EDIT.html' , context)

#edit recipe in the database

def editRecipe(request , id):
    if request.method == 'POST':
        newRname = request.POST.get('recipeName')
        newRingredients = request.POST.get('recipeIngredients')
        newRinstructions = request.POST.get('recipeInstructions')
        newRcourse = request.POST.get('courses')
        newRimage = request.FILES.get('recipeImage')

        #get the recipe to be edited
        editableRecipe = Recipe.objects.get(id = id)

        #update the data
        if newRname != '':
            editableRecipe.name = newRname

        if newRingredients != '':
            editableRecipe.ingredients = newRingredients
  
        if newRinstructions != '':
            editableRecipe.instructions = newRinstructions
        
        if newRcourse != '':
            editableRecipe.course_name = newRcourse

        if newRimage is not None:
            editableRecipe.image = newRimage

        #save the new data
        editableRecipe.save()

    return HttpResponseRedirect(reverse('adminHome'))



#__________________________________________________DYNAMICUSER/SEARCH/ADDTO FAV___________________________________________________#

#display a clicked recipe from the user OPENING PAGE:
def dispalyRecipe(request , id):
    displayedRecipe = Recipe.objects.get(id = id)
    context = {'Recipe' : displayedRecipe}
    return render(request , 'USER RECIPES.html' , context)


# ADD TO FAVOURITES
def add_to_fav(request, recipe_id):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = get_object_or_404(User, id=user_id)
        recipe = get_object_or_404(Recipe, id=recipe_id)
        fav=FavRecipes(userID=user,recipeID=recipe,recipe_NAME=recipe.name,recipe_image=recipe.image,course_name=recipe.course_name)
        if FavRecipes.objects.filter(userID=user_id,recipeID=recipe.id).exists():
            return HttpResponseRedirect(reverse('userHome'))
        else:
            fav.save()
            return HttpResponseRedirect(reverse('userHome'))
        
def show_favs(request):
    user_id = request.session.get('user_id')
    favourite_recipes=FavRecipes.objects.filter(userID=user_id)
    context={'fav_r':favourite_recipes}
    return render(request,'FAV_RECIPES.html',context)

def delete_fav_Recipe(request , id):
    fav_recipe = FavRecipes.objects.get(id=id)
    fav_recipe.delete()
    return HttpResponseRedirect(reverse('show_favs'))

#---------------------------------------SEARCH-------------------------------------#

def user_opening_page_view(request):
    recipes = Recipe.objects.all()
    recipes_list = [{
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'image': recipe.image.url if recipe.image else ''
    } for recipe in recipes]
    qs_json = json.dumps(recipes_list)
    return render(request, 'USER OPENNING PAGE.html', {'recipes_list': recipes_list, 'qs_json': qs_json})
