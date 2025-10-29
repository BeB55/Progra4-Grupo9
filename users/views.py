from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'users/login.html')

def home_view(request):
    return render(request, 'users/home.html')