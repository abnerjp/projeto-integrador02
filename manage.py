#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoIntegrador02.settings')

    # numero do twilio que ira enviar as mensagens
    os.environ.setdefault('BUSINESS_CELL_PHONE_WHATSAPP_TWILIO', '+14155238886')
    # numero do celular da barbearia que recebera as mensagens whatsapp
    os.environ.setdefault('RECEIVER_WHATSAPP_PHONE', '+5518981217469')
    # SID do para whatsapp
    os.environ.setdefault('TWILIO_ACCOUNT_SID', 'AC3d750ff48de7de048edb595c76759d31')

    # numero do celular da barbearia que recebera as mensagens sms
    os.environ.setdefault('RECEIVER_SMS_PHONE', '+5518981217469')
    # SID para sms
    os.environ.setdefault('TWILIO_MESSAGING_SERVICE_SID', 'MGbd7e5cee73304b53bc746e3d9110b72b')

    # deve ser obtido um novo... na conta twilio
    os.environ.setdefault('TWILIO_AUTH_TOKEN', '')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
