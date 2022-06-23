import requests
from django.shortcuts import render, redirect
from .utils.twilio_util import send_whatsapp_message, send_sms_message
from .utils.temporary import obter_servicos, obter_agenda, obter_horarios_disponiveis, \
    obter_servico_pelo_id, obter_instancia_servico_pelo_id
from .utils.validacoes import str_to_datetime, str_to_int, str_to_time, valida_celular
from .utils.utils import formatar_celular
from django.http import Http404
from datetime import *
from barbershop.dao.agenda_dao import Agenda_DAO


def verify_post_request(request):
    if not request.POST:
        raise Http404()

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

    dados_agendamento = request.session.get('dados_agendamento')
    if dados_agendamento is not None:
        del request.session['dados_agendamento']

    erros = request.session.get('erros')
    if erros is not None:
        del request.session['erros']

    context = {
        'consulta_active': 'active',
        'lista_servicos': obter_servicos(),
        'data_selecionada': data_selecionada,
        'erros': erros,
    }
    return render(request, 'barbershop/pages/inicio_agendamento.html', context)


def consulta_agenda(request):
    verify_post_request(request)

    erros = []
    data_convertida = str_to_datetime(request.POST.get('data_agendamento'))
    servico_id = str_to_int(request.POST.get('servico'))

    if data_convertida is None:
        erros.append("A data não é válida")

    servicos = []
    if servico_id is None:
        erros.append("O serviço selecionado não é válido")
    elif not len(erros) > 0:
        servicos = obter_servico_pelo_id(servico_id)
        if not len(servicos) > 0:
            erros.append("Não foi possível carregar o serviço selecionado")

    if len(erros) > 0:
        request.session['erros'] = erros
        return redirect('barbershop:inicio_agendamento')

    # horarios = obter_horarios()
    horarios  = obter_horarios_disponiveis(data_convertida.date(), servicos[0]['tempo_estimado'])

    request.session['dados_agendamento'] = {
        'data': data_convertida.date().isoformat(),
        'servico_id': servicos[0]['id'],
        'nome_servico': servicos[0]['nome'],
    }

    context = {
        'consulta_active': 'active',
        'lista_servicos': obter_servicos(),
        'data_selecionada': data_convertida.date().isoformat(),
        'servico_selecionado': servicos[0],
        'horarios': horarios,
    }
    return render(request, 'barbershop/pages/inicio_agendamento.html', context)


def pre_agendamento(request):
    verify_post_request(request)
    erros = []

    dados_agendamento = request.session.get('dados_agendamento')
    if dados_agendamento is None:
        erros.append("Não foi possível recuperar os dados informados")

    horario_selecionado = str_to_time(request.POST.get('horario_selecionado'))

    if horario_selecionado is None:
        erros.append("O horário selecionado não é válido")

    if len(erros) > 0:
        request.session['erros'] = erros
        return redirect('barbershop:inicio_agendamento')

    dados_agendamento['hora_agendada'] = horario_selecionado.isoformat()
    request.session['dados_agendamento'] = dados_agendamento

    print(dados_agendamento)

    context = {
        'consulta_active': 'active',
        'dados': dados_agendamento,
    }
    return render(request, 'barbershop/pages/agendamento.html', context)

def agendamento(request):
    erros = request.session.get('erros')
    if erros is not None:
        del request.session['erros']

    if erros is None:
        verify_post_request(request)

    context = {
        'consulta_active': 'active',
        'erros': erros,
    }
    return render(request, 'barbershop/pages/agendamento.html', context)


def confirmar_agendamento(request):
    verify_post_request(request)

    erros = []
    dados_agendamento = request.session.get('dados_agendamento')
    if dados_agendamento is None:
        erros.append("Não foi possível recuperar os dados informados nas telas anteriores")

    nome_cliente = request.POST.get('nome_cliente')
    telefone_celular = request.POST.get('telefone_celular')
    observacao_agendamento = request.POST.get('observacao')

    try:
        if len(nome_cliente) <= 3:
            erros.append("O nome deve conter pelo menos 3 caracteres")
    except:
        erros.append("O nome é obrigatório")

    # validar celular
    telefone_celular, msg_validacao_celular = valida_celular(telefone_celular)
    if msg_validacao_celular is not None:
        erros.append(msg_validacao_celular)

    if len(erros) > 0:
        request.session['erros'] = erros
        return redirect('barbershop:agendamento')

    dados_agendamento['nome_cliente'] = nome_cliente
    dados_agendamento['celular_cliente'] = formatar_celular(telefone_celular)
    dados_agendamento['observacao_cliente'] = observacao_agendamento

    del request.session['dados_agendamento']

    telefone_celular = "+55" + telefone_celular

    nova_agenda = Agenda_DAO(
        servico=obter_instancia_servico_pelo_id(dados_agendamento['servico_id']),
        data_agenda=dados_agendamento['data'],
        nome_cliente=dados_agendamento['nome_cliente'],
        celular_cliente=telefone_celular,
        hora_inicio=dados_agendamento['hora_agendada']
    )

    nova_agenda.salvar()

    # envia mensagem layout para que a próxima mensagem possa ser enviada - whatsapp
    send_whatsapp_message("Your UUID report code is " + nova_agenda.codigo_uuid)
    send_whatsapp_message(observacao_agendamento)



    # envia mensagem - sms
    # send_sms_message(observacao_agendamento, telefone_celular)

    context = {
        'consulta_active': 'active',
        'dados': dados_agendamento,
    }
    return render(request, 'barbershop/pages/fim_agendamento.html', context)


def fim_agendamento(request):
    dados_agendamento = request.session.get('dados_agendamento')
    if dados_agendamento is not None:
        del request.session['dados_agendamento']

    return render(request, 'barbershop/pages/fim_agendamento.html')
