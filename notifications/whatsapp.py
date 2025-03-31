from twilio.rest import Client

class WhatsAppNotifier:
    def __init__(self, account_sid, auth_token, from_whatsapp, to_whatsapp):
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp = from_whatsapp
        self.to_whatsapp = to_whatsapp

    def send_message(self, message):
        self.client.messages.create(
            body=message,
            from_=self.from_whatsapp,
            to=self.to_whatsapp
        )
