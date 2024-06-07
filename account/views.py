from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import IntegrityError


def register__view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            try:
                newUser = User(username=username)
                newUser.set_password(password)
                newUser.save()
                login(request, newUser)
                messages.success(request, "Siz qeydiyyatdan keçdiniz.")
                return redirect("home")
            except IntegrityError:
                messages.error(request, "Bu istifadəçi adı artıq mövcuddur. Zəhmət olmasa başqa bir istifadəçi adı seçin.")
            except Exception as e:
                messages.error(request, f"Qeydiyyat zamanı bir xəta baş verdi: {e}")
    
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login__view(request):
    form = LoginForm(request.POST or None)
    
    context = {"form": form}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return render(request, "login.html", context)
        
        login(request, user)
        messages.success(request, "Siz daxil oldunuz.")
        return redirect("home")
    return render(request, "login.html", context)


def logout__view(request):
    logout(request)
    return redirect("home")