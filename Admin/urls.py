from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', inicio, name='productos'),
    path('nuevo-producto', nuevo, name='nuevo'),
]