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