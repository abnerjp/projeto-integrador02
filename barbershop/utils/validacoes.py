import re
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


def str_to_time(value):
    valor_convertido = None
    try:
        valor_convertido = time.fromisoformat(value)
    except:
        ...
    return valor_convertido

def valida_celular(value):
    erro = None
    valor_retorno = value

    somente_numeros = re.sub(r'\D', '', value)
    if len(somente_numeros) < 11:
        erro = "O número de celular informado não é válido."
    else:
        valor_retorno = somente_numeros[-11:]

    return valor_retorno, erro