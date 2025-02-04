import requests

SHEETY_GET_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices"
SHEETY_POST_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices"
SHEETY_PUT_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices/[Object ID]"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_request = requests.get(url=SHEETY_GET_URL)
        self.sheet_data = self.sheet_request.json()["prices"]

    def iata_search(self):
        if self.sheet_data["iataCode"] == "":
            pass
            # TODO: How are you going to update iataCode with a new result?