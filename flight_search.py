import requests
import os

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TEQUILA_APIKEY = os.getenv("TEQUILA_APIKEY")


class FlightSearch:

    def get_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_APIKEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
