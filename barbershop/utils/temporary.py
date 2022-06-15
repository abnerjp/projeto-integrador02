
def get_list_services():
    return [
        'Corte de cabelo',
        'Corte de barba',
        'Escova progressiva',
        'Manicure/Pedicure',
        'Hidratação',
    ]

def get_dict_services():
    dict = {}
    i = 1
    for service in get_list_services():
        dict.setdefault(i, service)
        i += 1
    return dict
