from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm

from rest_framework import viewsets
from .forms import CustomUserCreationForm, AvatarForm, LoginForm
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

def home_view(request):
    return render(request, '../templates/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # o '/' si preferís
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.cleaned_data["user"]
        login(request, user)
        return redirect('home')

    return render(request, 'users/login.html', {'form': form})

def signout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile_view(request):
    return render(request, 'users/profile.html')

def edit_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AvatarForm(instance=request.user)
    return render(request, 'users/edit_avatar.html', {'form': form})