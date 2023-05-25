from twilio.rest import Client


def send_sms(message):
    # Twilio account information
    account_sid = ''
    auth_token = ''
    twilio_phone_number = ''
    client = Client(account_sid, auth_token)
    # Use Twilio to send an SMS message to the phone
    message = client.messages.create(
        to='',
        from_=twilio_phone_number,
        body=message
    )

    return "message sent"
