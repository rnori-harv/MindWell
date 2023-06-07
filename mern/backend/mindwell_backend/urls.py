from django.urls import path, include
from . import views

urlpatterns = [
    path('create-entry/', views.create_entry, name='create_entry')
    ]


SUFFIX = [
    'localhost',
    'api/create-entry/',
]