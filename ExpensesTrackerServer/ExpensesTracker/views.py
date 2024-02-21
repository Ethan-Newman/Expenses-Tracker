# ExpensesTrackerServer/your_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('home')  # Update with your home URL name
    else:
        form = LoginForm()

    return render(request, 'ExpensesTracker/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with your home view name

# This will be a home-view dashboard in the future.
def home_view(request):
    return render(request, 'ExpensesTracker/home.html')

def expenses_view(request):
    return render(request, 'ExpensesTracker/expenses.html')

def income_view(request):
    return render(request, 'ExpensesTracker/income.html')

def analytics_view(request):
    return render(request, 'ExpensesTracker/analytics.html')

def data_view(request):
    return render(request, 'ExpensesTracker/data.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password == confirm_password:
            # Create a new user
            User.objects.create_user(username=username, password=password)

            # Redirect to a success page or login page
            return redirect('login')  # Assuming you have a 'login' URL name

        else:
            # Passwords don't match, handle this case as needed
            return render(request, 'ExpensesTracker/signup.html', {'error': 'Passwords do not match'})

    return render(request, 'ExpensesTracker/signup.html')