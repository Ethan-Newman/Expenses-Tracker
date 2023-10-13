from django.shortcuts import render

# views.py

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # For simplicity; in a real-world scenario, use a proper CSRF protection
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        # Add your authentication logic here
        if username == 'user' and password == 'pass':
            return HttpResponse(json.dumps({'message': 'Login successful'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': 'Invalid username or password'}), content_type='application/json')

    return HttpResponse(json.dumps({'error': 'Invalid request method'}), content_type='application/json')

