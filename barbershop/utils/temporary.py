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


def obter_servicos():
    return obter_servicos_do_bd()


def obter_servico_pelo_id(service_id):
    return criar_lista_de_servicos(
        Servico.objects.filter(ativo=True, id=service_id).order_by('nome')
    )


def obter_instancia_servico_pelo_id(service_id):
    return Servico.objects.filter(ativo=True, id=service_id)[0]


def obter_toda_agenda_por_dia(data_consultada=datetime.today()):
    horarios_agendados = Agenda.objects.filter(
        data_hora_inicio__date=data_consultada
    ).order_by('data_hora_inicio')
    return horarios_agendados

def obter_agenda_por_dia(nao_confirmado=False, data_consultada=datetime.today()):
    horarios_agendados = Agenda.objects.filter(
        data_hora_confirmacao__isnull=nao_confirmado,
        data_hora_inicio__date=data_consultada
    ).order_by('data_hora_inicio')
    return horarios_agendados

# método foi desenvolvido mas nao esta sendo utilizado
# obtem as agendas confirmadas do dia informado, e verifica se o horario analisado esta disponivel
def horario_disponivel(data, horario_analisado_inicio, tempo_servico_selecionado=time(0, 30, 0)):
    disponivel = True

    delta_tempo_servico = timedelta(
        hours=+tempo_servico_selecionado.hour,
        minutes=+tempo_servico_selecionado.minute,
        seconds=+tempo_servico_selecionado.second
    )

    # busca todos os horarios já confirmados do dia
    horarios_confirmado = obter_agenda_por_dia(nao_confirmado=False, data_consultada=data)

    analisado_inicio = datetime.combine(data, horario_analisado_inicio)
    analisado_fim = analisado_inicio + delta_tempo_servico

    for horario_confirmado in horarios_confirmado:
        confirmado_inicio = horario_confirmado['data_hora_inicio']
        confirmado_fim = horario_confirmado['data_hora_fim']

        if confirmado_inicio >= analisado_inicio and confirmado_inicio < analisado_fim:
            disponivel = False
            break

        if confirmado_fim > analisado_inicio and confirmado_fim <= analisado_fim:
            disponivel = False
            break

        if analisado_inicio >= confirmado_inicio and analisado_inicio < confirmado_fim:
            disponivel = False
            break

        if analisado_fim > confirmado_inicio and analisado_fim <= confirmado_fim:
            disponivel = False
            break

    return disponivel


def obter_horarios_disponiveis():
    lista_horarios = []
    for i in range(8, 18):
        if i != 12:
            disponivel = True
        else:
            disponivel = False

        horario_analisado = time(i, 0, 0)
        lista_horarios.append({
            'horario': horario_analisado,
            'disponivel': disponivel
        })

        horario_analisado = time(i, 30, 0)
        lista_horarios.append({
            'horario': horario_analisado,
            'disponivel': disponivel
        })
    return lista_horarios

def obter_agenda_por_uuid(codigo_uuid_procurado):
    horario = None
    try:
        horario = Agenda.objects.get(
            codigo_uuid=codigo_uuid_procurado
        )
    except:
        ...
    return horario