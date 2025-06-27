from django.urls import path
from .views import index, usuarios

urlpatterns = [
    path('', index, name='index'),
    path('usuarios/', usuarios, name='usuarios'),
]
