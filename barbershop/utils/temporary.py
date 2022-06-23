from barbershop.models import Servico, Agenda
from datetime import *

def criar_lista_de_servicos(servicos):
    lista_servicos = []
    for servico in servicos:
        lista_servicos.append({
            'id': servico.id,
            'nome': servico.nome,
            'tempo_estimado': servico.tempo_estimado,
        })
    return lista_servicos

def obter_servicos_do_bd():
    return criar_lista_de_servicos(
        Servico.objects.filter(ativo=True).order_by('nome')
    )

def obter_servicos_moc():
    list_services = [
        'Corte de cabelo',
        'Corte de barba',
        'Escova progressiva',
        'Manicure/Pedicure',
        'Hidratação',
    ]
    dict = {}
    i = 1
    for service in list_services:
        dict.setdefault(i, service)
        i += 1
    return dict

def obter_servicos():
    return obter_servicos_do_bd()

def obter_servico_pelo_id(service_id):
    return criar_lista_de_servicos(
        Servico.objects.filter(ativo=True, id=service_id).order_by('nome')
    )

def obter_instancia_servico_pelo_id(service_id):
    return Servico.objects.filter(ativo=True, id=service_id)[0]

def obter_agenda(data_consultada=datetime.today()):
    horarios_agendados = Agenda.objects.filter(
        data_hora_confirmacao__isnull=False,
        data_hora_inicio__date=data_consultada
    ).order_by('data_hora_inicio')

    lista_horarios_agendados = []
    for horario_agendado in horarios_agendados:
        lista_horarios_agendados.append({
            'data_hora_inicio': horario_agendado.data_hora_inicio,
            'data_hora_fim': horario_agendado.data_hora_fim,
        })

    return lista_horarios_agendados

def obter_horarios():
    lista_horarios = []
    for i in range(8, 18):
        if i != 12:
            lista_horarios.append(time(i, 0, 0))
            lista_horarios.append(time(i, 30, 0))

    return lista_horarios
