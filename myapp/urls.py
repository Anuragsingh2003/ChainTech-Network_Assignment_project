from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('submit/', handle_form_submission, name='submit'),
    path('confirmation/', confirmation, name='confirmation'),


]
