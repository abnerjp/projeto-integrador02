from barbershop.models import Servico

def get_services_from_bd():
    servicos = Servico.objects.filter(ativo=True).order_by('nome')

    lista_servicos = []
    for servico in servicos:
        lista_servicos.append({
            'id': servico.id,
            'nome': servico.nome,
            'tempo_estimado': servico.tempo_estimado,
        })

    return lista_servicos

def get_services_moc():
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

def get_services():
    return get_services_from_bd()

