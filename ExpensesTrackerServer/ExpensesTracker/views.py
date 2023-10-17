# ExpensesTrackerServer/your_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or home
            return redirect('home')  # Change 'home' to your actual home URL name
    else:
        form = AuthenticationForm()
    return render(request, 'ExpensesTracker/login.html', {'form': form})

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
    return render(request, 'ExpensesTracker/signup.html')
