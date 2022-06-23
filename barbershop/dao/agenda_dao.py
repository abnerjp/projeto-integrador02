from barbershop.models import Agenda
from datetime import *
import uuid
import re

class Agenda_DAO:

    def __init__(self, servico, nome_cliente, celular_cliente, data_agenda, hora_inicio):
        self.servico = servico
        self.nome_cliente = nome_cliente
        self.celular_cliente = celular_cliente
        self.data_hora_inicio = self.__gerar_datetime(data_agenda, hora_inicio)
        self.data_hora_fim = self.__calcular_hora_fim()
        self.codigo_uuid = self.__make_uuid()

    def salvar(self):
        Agenda(
            data_hora_inicio=self.data_hora_inicio,
            data_hora_fim=self.data_hora_fim,
            nome_cliente=self.nome_cliente,
            celular_cliente=self.celular_cliente,
            servico=self.servico,
            codigo_uuid=self.codigo_uuid,
        ).save()

    def __calcular_hora_fim(self):
        tempo_servico = self.servico.tempo_estimado
        tdelta = timedelta(
            hours=+tempo_servico.hour,
            minutes=+tempo_servico.minute,
            seconds=+tempo_servico.second,
        )
        return self.data_hora_inicio + tdelta

    def __gerar_datetime(self, data_agenda, hora_inicio):
        return datetime.combine(
            date.fromisoformat(data_agenda),
            time.fromisoformat(hora_inicio)
        )

    def __make_uuid(self):
        return re.sub(r'-', '', str(uuid.uuid4()))
