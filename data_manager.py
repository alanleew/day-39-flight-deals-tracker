import requests

SHEETY_GET_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices"
SHEETY_POST_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices"
SHEETY_PUT_URL = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/flightDeals/prices/[Object ID]"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheet_request = requests.get(url=SHEETY_GET_URL)
    json_data = sheet_request.json()

    # def edit_row(self):