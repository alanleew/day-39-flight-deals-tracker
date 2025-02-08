import os
from dotenv import load_dotenv
import requests

load_dotenv()

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_header = {
            "Authorization": f"Basic {SHEETY_KEY}"
        }
        self.sheet_data = {}

    def get_data(self):
        sheet_response = requests.get(url=SHEETY_URL, headers=self.sheety_header)
        # sheet_response.raise_for_status()
        json = sheet_response.json()
        self.sheet_data = json["prices"]
        return self.sheet_data

    def update_sheet(self, row):
        SHEETY_PUT_URL = f"{SHEETY_URL}/{row["id"]}"
        body = {
            "price": row
        }
        response = requests.put(url=SHEETY_PUT_URL, json=body, headers=self.sheety_header)
        response.raise_for_status()
        print(response.text)