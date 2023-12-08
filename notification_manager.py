from twilio.rest import Client
import os

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_NUM = os.getenv("TWILIO_NUM")
MY_NUM = os.getenv("MY_NUM")


class NotificationManager:
    def send_notif(self, price, city_to, iata_code, from_date, to_date):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body= f"Low Price Alert!✈️ Only ₹{price} to fly from Bangalore-BLR to {city_to}-{iata_code}, "
                  f"from {from_date} to {to_date} ",
            from_=TWILIO_NUM,
            to=MY_NUM
        )

        print(message.sid)
