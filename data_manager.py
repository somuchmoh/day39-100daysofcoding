import requests
import os

username = os.getenv("SHEETY_USERNAME")
sheet_name = os.getenv("SHEETY_SHEETNAME")
sheet = os.getenv("SHEETY_SHEET")
sheety_url = f"https://api.sheety.co/{username}/{sheet_name}/{sheet}/"
sheety_auth = f"Bearer {os.getenv("SHEETY_AUTH")}"
header = {"Authorization": sheety_auth}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_url, headers=header)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_sheet(self, row_id, body):
        url = f"{sheety_url}/{row_id}"
        requests.put(url=url, json=body, headers=header)
