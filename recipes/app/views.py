from django.shortcuts import render
from .forms import RecipeForm
from django.contrib import messages
from .models import Recipe
# Create your views here.

def home_recipe(request):
    all_recipes=Recipe.objects.all()
    return render(request,'app/recipe_home.html',{'recipes':all_recipes})

def add_recipe(request):
    if request.method=='POST':
        form=RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Recipe added to the Library ")
            form=RecipeForm()
            return render(request,"app/add_recipe.html",{'form':form})
    else:
        form=RecipeForm()
    return render(request,"app/add_recipe.html",{'form':form})
