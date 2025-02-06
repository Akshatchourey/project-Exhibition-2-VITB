from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'pahal/index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists.")
            return redirect(request, '/register/')

        user = User.objects.create_user(
            first_name = first_name,
            email = email,
            username = username
        )
        user.set_password(password)
        user.save()

        return redirect('/login/')

    return render(request, 'pahal/signup.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Incorrect password")
            return redirect(request, '/login/')
        else:
            login(request, user)
            return redirect("/")

    return render(request, 'pahal/login.html')
def logout_page(request):
    logout(request)
    return redirect('/')
