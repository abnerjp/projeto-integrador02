import requests
from django.shortcuts import render, redirect
from .utils.twilio_util import send_whatsapp_message, send_sms_message
from .utils.temporary import obter_servicos, obter_agenda, obter_horarios, obter_servico_pelo_id
from .utils.validar_campos import valida_campos, str_to_datetime, str_to_int
from django.http import Http404
from datetime import date, datetime


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
        'lista_servicos': obter_servicos(),
        'data_selecionada': data_selecionada,
    }
    return render(request, 'barbershop/pages/inicio_agendamento.html', context)


def consulta_agenda(request):
    if not request.POST:
        raise Http404()
    data_informada = request.POST.get('data_agendamento')
    servico_selecionado = request.POST.get('servico')

    sao_campos_validos, data_convertida, servico_id = valida_campos(data_informada, servico_selecionado)
    if sao_campos_validos:
        servico = obter_servico_pelo_id(servico_id)

    sao_campos_validos = sao_campos_validos and len(servico) > 0

    if not sao_campos_validos:
        return redirect('barbershop:inicio_agendamento')

    horarios = obter_horarios()

    context = {
        'consulta_active': 'active',
        'lista_servicos': obter_servicos(),
        'data_selecionada': data_convertida.date().isoformat(),
        'servico_selecionado': servico[0],
        'horarios': horarios,
    }
    return render(request, 'barbershop/pages/inicio_agendamento.html', context)
    # return redirect('barbershop:agendamento')


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

    # envia mensagem - whatsapp
    # sid = send_whatsapp_message(
    #     content_body=observacao_agendamento,
    #     from_number=telefone_celular
    # )

    # envia mensagem - sms
    # sid = send_sms_message(
    #     content_body=observacao_agendamento,
    #     from_number=telefone_celular
    # )
    # print(sid)

    return redirect('barbershop:fim_agendamento')


def fim_agendamento(request):
    return render(request, 'barbershop/pages/fim_agendamento.html')
