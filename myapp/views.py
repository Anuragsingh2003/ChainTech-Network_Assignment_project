from django.shortcuts import render, redirect
from .models import UserData
import random
import requests

def get_dynamic_content():
    api_url = "https://api.quotable.io/random"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        data = response.json()
        quote = f"{data['content']} - {data['author']}"
        return quote
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return "Error fetching quote"

def index(request):
    dynamic_content = get_dynamic_content()
    return render(request, 'index.html', {'dynamic_content': dynamic_content})


# def handle_form_submission(request):
#     if request.method == 'POST':
#         # Process form data here
#         return render(request, 'confirmation.html', {'data': request.POST})


def handle_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        # Save form data to the database
        UserData.objects.create(name=name, email=email)

        return redirect('confirmation')
    return render(request, 'index.html')


def confirmation(request):
    # Retrieve and display stored data
    user_data_list = UserData.objects.all()
    return render(request, 'confirmation.html', {'user_data_list': user_data_list})