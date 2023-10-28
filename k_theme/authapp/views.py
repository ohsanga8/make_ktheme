from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                messages.error(request, "User creation failed.")
        else:
            messages.error(request, "Invalid from data.")
            # username = form.cleaned_data.get("username")
            # raw_password = form.cleaned_data.get("password1")
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "authapp/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main")
    else:
        form = CustomAuthenticationForm()
    return render(request, "authapp/login.html", {"form": form})
