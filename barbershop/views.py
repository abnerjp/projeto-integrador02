import requests
import os
from django.shortcuts import render, redirect, resolve_url
from .utils.twilio_util import send_whatsapp_message, send_sms_message
from .utils.temporary import obter_servicos, obter_toda_agenda_por_dia, obter_horarios_disponiveis, \
    obter_servico_pelo_id, obter_instancia_servico_pelo_id, obter_agenda_por_uuid
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

    horarios = obter_horarios_disponiveis()

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
        observacao_cliente=observacao_agendamento,
        hora_inicio=dados_agendamento['hora_agendada']
    )

    nova_agenda.salvar()

    url_confirmacao = request.build_absolute_uri(
        resolve_url('barbershop:confirmacao_registro', nova_agenda.codigo_uuid)
    )

    # envia mensagem layout para que a próxima mensagem possa ser enviada - whatsapp
    wpp_msg = "Your NEW_CONFIRMATION code is " + nova_agenda.codigo_uuid
    send_whatsapp_message(wpp_msg)

    sms_msg = "-= Yeshua =-\nNova solicitação\n\n" + url_confirmacao
    send_sms_message(sms_msg, telefone_celular)

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


def validar_agenda(request, codigo_uuid):
    horario_analisado = obter_agenda_por_uuid(str(codigo_uuid))

    if horario_analisado is None:
        return redirect('barbershop:home')

    dados = {
        'nome_cliente': horario_analisado.nome_cliente,
        'nome_servico': horario_analisado.servico.nome,
        'observacao_cliente': horario_analisado.observacao_cliente,
        'data_hora_inicio': horario_analisado.data_hora_inicio,
        'data_hora_fim': horario_analisado.data_hora_fim,
        'telefone_celular': formatar_celular(horario_analisado.celular_cliente),
        'codigo_uuid': horario_analisado.codigo_uuid,
        'horario_ja_confirmado': horario_analisado.data_hora_confirmacao is not None,
    }

    horarios_do_dia = []
    horarios_cadastrados = obter_toda_agenda_por_dia(data_consultada=horario_analisado.data_hora_inicio)
    for horario_agendado in horarios_cadastrados:
        horario_confirmado = horario_agendado.data_hora_confirmacao is not None
        sendo_analisado = horario_agendado.codigo_uuid == horario_analisado.codigo_uuid
        url_confirmacao = None
        if not horario_confirmado:
            url_confirmacao = request.build_absolute_uri(
                resolve_url('barbershop:confirmacao_registro', horario_agendado.codigo_uuid)
            )
        horarios_do_dia.append({
            'nome_servico': horario_agendado.servico.nome,
            'data_hora_inicio': horario_agendado.data_hora_inicio,
            'data_hora_fim': horario_agendado.data_hora_fim,
            'sendo_analisado': sendo_analisado,
            'horario_ja_confirmado': horario_agendado.data_hora_confirmacao is not None,
            'link_aprovacao': url_confirmacao,
        })

    context = {
        'dados': dados,
        'agenda_do_dia': horarios_do_dia,
    }

    return render(request, 'barbershop/pages/validar_agenda.html', context)


def confirmacao_agenda_pelo_dono(request):
    verify_post_request(request)
    codigo_uuid = request.POST.get('codigo_uuid')

    horario_analisado = obter_agenda_por_uuid(str(codigo_uuid))
    if horario_analisado is None:
        return redirect('barbershop:home')

    horario_analisado.data_hora_confirmacao = datetime.today()
    horario_analisado.save()

    sms_msg = "-= Yeshua =-\n" \
              "Seu horário foi confirmado\n" \
              "Serviço: " + horario_analisado.servico.nome + "\n" \
              "Data: " + horario_analisado.data_hora_inicio.strftime('%d/%m/%Y, %Hh%M %p')
    # envia mensagem - sms
    send_sms_message(sms_msg, horario_analisado.celular_cliente)

    return redirect('barbershop:confirmacao_registro', codigo_uuid)
