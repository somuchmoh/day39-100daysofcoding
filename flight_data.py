from datetime import datetime, timedelta
import requests
import os

FLIGHT_URL = os.getenv("FLIGHT_URL")
DATE_FROM_FLY = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
DATE_TO_FLY = (datetime.now() + timedelta(days=120)).strftime("%d/%m/%Y")
TEQUILA_APIKEY = os.getenv("TEQUILA_APIKEY")


class FlightData:
    def get_data(self, city):
        flight_header = {"apikey": TEQUILA_APIKEY}
        flight_data = {
            "fly_from": "BLR",
            "fly_to": city,
            "date_from": DATE_FROM_FLY,
            "date_to": DATE_TO_FLY,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 15,
            "curr": "INR",
            "max_stopovers": 0,
            "limit": 1
        }
        flight_response = requests.get(url=FLIGHT_URL, headers=flight_header, params=flight_data)
        results = flight_response.json()
        return results


