from django.shortcuts import render, redirect
from .models import Product , Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm

def HelloWorld(request):
    all_products = Product.objects.all()

    return render(request, "index.html", {"products": all_products})


def about(request):
    return render(request, "about.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successfully"))
            return redirect("home")
        else:
            messages.error(request, ("Login Error"))
            return redirect("login")
    else:
    
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("home")

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1= form.cleaned_data['password1']
            user.set_password(password1)
            user.save()

            user = authenticate(username=user.username, password=password1)
            
            if user is not None:
                login(request, user)
                messages.success(request, ("Registration Successful"))
                return redirect("home")
        else:
            messages.error(request, ("Registration Error"))
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})
    
def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {"product": product}

    return render(request, "product.html", context)

def category(request, cat):
    cat = cat.replace("-", " ") 
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {"category": category, "products": products})
    except:
        return redirect("home")
    products = Product.objects.filter(category=cat)
