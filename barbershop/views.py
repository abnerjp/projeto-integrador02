from django.shortcuts import render, redirect
from django.http import Http404

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
        'consulta_active': 'active',
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


def confirmar_agendamento(request):
    if not request.POST:
        raise Http404()

    nome_cliente = request.POST.get('nome_cliente')
    telefone_celular = request.POST.get('telefone_celular')
    observacao_agendamento = request.POST.get('observacao')

    return redirect('barbershop:consulta_agenda')



