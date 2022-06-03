from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'barbershop/pages/home.html')

def galeria(request):
    return render(request, 'barbershop/pages/galeria.html')

def catalogo(request):
    return render(request, 'barbershop/pages/catalogo.html')

def agendamento(request):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dias_mes = range(1, 32)

    context = {
        'meses': meses,
        'dias_do_mes': dias_mes,
    }
    return render(request, 'barbershop/pages/agendamento.html', context)
