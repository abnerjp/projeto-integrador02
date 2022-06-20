from datetime import datetime, time


def str_to_datetime(value):
    valor_convertido = None
    try:
        valor_convertido = datetime.strptime(value, "%Y-%m-%d")
    except:
        ...
    return valor_convertido


def str_to_int(value):
    valor_convertido = None
    try:
        valor_convertido = int(value)
    except:
        ...
    return valor_convertido


def valida_campos(data, servico_id):
    data_testada = str_to_datetime(data)
    id_testado = str_to_int(servico_id)
    valido = data_testada is not None and id_testado is not None

    return valido, data_testada, id_testado
