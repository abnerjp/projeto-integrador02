from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'home_active': 'active',
    }
    return render(request, 'barbershop/pages/home.html', context)

def galeria(request):
    context = {
        'galeria_active': 'active',
    }
    return render(request, 'barbershop/pages/galeria.html', context)

def catalogo(request):
    context = {
        'catalogo_active': 'active',
    }
    return render(request, 'barbershop/pages/catalogo.html', context)

def agendamento(request):
    context = {
        'agendamento': 'active',
    }
    return render(request, 'barbershop/pages/agendamento.html', context)

def consulta_agenda(request):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dias_mes = range(1, 32)

    context = {
        'consulta_active': 'active',
        'meses': meses,
        'dias_do_mes': dias_mes,
    }
    return render(request, 'barbershop/pages/consulta_agenda.html', context)
