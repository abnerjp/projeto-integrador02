from django.shortcuts import render, redirect
from .utils.twilio_util import send_whatsapp_message, send_sms_message
from .utils.temporary import get_list_services, get_dict_services
from django.http import Http404
from datetime import date

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


def inicio_agendamento(request):
    data_selecionada = date.today().isoformat()

    context = {
        'consulta_active': 'active',
        'servicos': get_dict_services(),
        'data_selecionada': data_selecionada,
    }
    return render(request, 'barbershop/pages/inicio_agendamento.html', context)


def consulta_agenda(request):
    if not request.POST:
        raise Http404()

    print('Consulta agenda:', request.POST)

    return redirect('barbershop:agendamento')


def agendamento(request):
    context = {
        'consulta_active': 'active',
    }
    return render(request, 'barbershop/pages/agendamento.html', context)


def confirmar_agendamento(request):
    if not request.POST:
        raise Http404()

    nome_cliente = request.POST.get('nome_cliente')
    telefone_celular = request.POST.get('telefone_celular')
    observacao_agendamento = request.POST.get('observacao')

    # sid = send_whatsapp_message(
    #     content_body=observacao_agendamento,
    #     from_number=telefone_celular
    # )

    sid = send_sms_message(
        content_body=observacao_agendamento,
        from_number=telefone_celular
    )
    print(sid)
    return redirect('barbershop:consulta_agenda')



