import os
from twilio.rest import Client

def send_whatsapp_message(content_body, from_number):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=content_body,
        to='whatsapp:+5518981217469'
    )
    return message.sid


def send_sms_message(content_body, from_number='+5518981217469'):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # sms_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID_FIRST']
    sms_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID_SECOND']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid=sms_service_sid,
        body=content_body,
        to=from_number
    )
    return message.sid
