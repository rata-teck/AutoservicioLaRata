from urllib import request
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "admin/listado.html")
def nuevo(request):
    return render(request, "admin/agregar.html")