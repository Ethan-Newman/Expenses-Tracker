# ExpensesTrackerServer/your_app/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # You can customize the form if needed
    pass
