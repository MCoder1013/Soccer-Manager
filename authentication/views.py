from django.shortcuts import render

# Create your views here.
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from players.models import Team
from .models import *


# Define a view function for the home page
def home(request):
    return render(request, 'main.html')

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('login_page')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('login_page')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')

    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        team_id = request.POST.get('team')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('register')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Create UserProfile with selected team
        team = Team.objects.get(id=team_id)
        UserProfile.objects.create(user=user, team=team)

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('login_page')

    # Pass teams to the template for selection
    teams = Team.objects.all()
    return render(request, 'register.html', {'teams': teams})

@login_required
def user_profile(request):
    profile = request.user.userprofile
    return render(request, "authentication/user_profile.html", {"profile": profile})


