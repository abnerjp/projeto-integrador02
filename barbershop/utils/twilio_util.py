import os
from twilio.rest import Client

def send_whatsapp_message(content_body):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    sender_cell_phone = os.environ.get('BUSINESS_CELL_PHONE_WHATSAPP_TWILIO')
    receiver_cell_phone = os.environ.get('RECEIVER_WHATSAPP_PHONE')
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            from_='whatsapp:' + sender_cell_phone,
            body=content_body,
            to='whatsapp:' + receiver_cell_phone
        )
        return message.sid
    except:
        return None


def send_sms_message(content_body, to_number=os.environ.get('RECEIVER_SMS_PHONE')):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # sms_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID_FIRST']
    sms_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID_SECOND']

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            messaging_service_sid=sms_service_sid,
            body=content_body,
            to=to_number
        )
        return message.sid
    except:
        return None
