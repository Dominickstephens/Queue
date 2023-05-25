from twilio.rest import Client


def send_sms(message):
    # Twilio account information
    account_sid = 'ACadea9ab1559315197d5fa4cabf1f99ce'
    auth_token = 'e157fdf41a05f1a7276bbc65dc13dfbd'
    twilio_phone_number = '+13204094973'
    client = Client(account_sid, auth_token)
    # Use Twilio to send an SMS message to the phone
    message = client.messages.create(
        to='+353858306021',
        from_=twilio_phone_number,
        body=message
    )

    return "message sent"
