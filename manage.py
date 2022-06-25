#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoIntegrador02.settings')
    os.environ.setdefault('BUSINESS_CELL_PHONE_WHATSAPP_TWILIO', '+14155238886')
    os.environ.setdefault('RECEIVER_WHATSAPP_PHONE', '+5518981217469')
    os.environ.setdefault('RECEIVER_SMS_PHONE', '+5518981217469')
    os.environ.setdefault('TWILIO_ACCOUNT_SID', '')
    os.environ.setdefault('TWILIO_MESSAGING_SERVICE_SID_FIRST', '')
    os.environ.setdefault('TWILIO_MESSAGING_SERVICE_SID_SECOND', '')
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
