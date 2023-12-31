# ExpensesTrackerServer/your_app/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('expenses/', expenses_view, name='expenses'),
    path('income/', income_view, name='income'),
    path('analytics/', analytics_view, name='analytics'),
    path('data/', data_view, name='data'),
    path('login/', login_view, name='login'),
    # Add other URL patterns as needed
]
