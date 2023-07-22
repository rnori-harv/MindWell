from django.urls import path, include
from . import views

urlpatterns = [
    path('create-entry/', views.create_entry, name='create_entry'),
    path('api_key/submit/', views.submit_api_key, name='submit_api_key')
    ]


SUFFIX = [
    'localhost',
    'api/create-entry/',
    'api/api_key/submit/'
]