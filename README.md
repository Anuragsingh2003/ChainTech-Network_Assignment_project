# My Django Web Project

This repository contains a simple Django web project with exercises to create a basic web page, set up a Python web server, add dynamic content, handle forms, and implement data persistence.

## Exercise 1: Setting Up a Simple Web Page

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-django-project.git
   cd your-django-project
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver


your-django-project/
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── migrations/
│   │   ├── __init__.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── confirmation.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   ├── confirmation.html
│   └── index.html
├── manage.py
├── requirements.txt
└── README.md
