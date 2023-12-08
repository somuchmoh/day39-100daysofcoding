import requests
import os


class DataManager:
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.sheet_name = os.getenv("SHEETY_SHEETNAME")
        self.sheet = os.getenv("SHEETY_SHEET")
        self.sheety_url = f"https://api.sheety.co/{self.username}/{self.sheet_name}/{self.sheet}"
        self.sheety_auth = f"Bearer {os.getenv("SHEETY_AUTH")}"
        self.header = {"Authorization": self.sheety_auth}
        self.response = requests.get(url=self.sheety_url, headers=self.header).json()
        self.prices = self.response['prices']


    def update_sheet(self, row_id, body):
        url = f"{self.sheety_url}/{row_id}"
        requests.put(url=url, json=body, headers=self.header)

