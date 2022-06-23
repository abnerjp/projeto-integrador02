import re

def formatar_celular(value):
    numero_formatado = "("+value[:2]+") "+value[2:7]+"-"+value[-4:]
    return numero_formatado;