import os
from dotenv import load_dotenv
import requests

load_dotenv()

AMADEUS_API_KEY=os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET=os.getenv("AMADEUS_API_SECRET")
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
AMADEUS_ACCESS_TOKEN_URL = f"{AMADEUS_ENDPOINT}/security/oauth2/token"
AMADEUS_CITY_SEARCH_URL = f"{AMADEUS_ENDPOINT}/reference-data/locations/cities"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._token = self.get_new_token()

    def search(self, row):
        if row["iataCode"] == "":
            row["iataCode"] = "TESTING"

    def get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_data = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET
        }

        token_response = requests.post(url=AMADEUS_ACCESS_TOKEN_URL, headers=header, data=token_data)
        return token_response.json()["access_token"]

