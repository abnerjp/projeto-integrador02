from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'barbershop/pages/home.html')

def galeria(request):
    return render(request, 'barbershop/pages/galeria.html')

