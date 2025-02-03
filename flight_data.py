import requests

AMADEUS_API_KEY = "J3qIq6IWQ4wKvnLUxC9a7dxAFCMfJeAE"
AMADEUS_API_SECRET = "fvyOcjZjSubZTbzN"
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
AMADEUS_ACCESS_TOKEN_URL = f"{AMADEUS_ENDPOINT}/security/oauth2/token"
AMADEUS_CITY_SEARCH_URL = f"{AMADEUS_ENDPOINT}/reference-data/locations/cities"

class FlightData:
    # This class is responsible for structuring the flight data.
    token_data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET
    }

    token_request = requests.post(url=AMADEUS_ACCESS_TOKEN_URL, data=token_data)
    amadeus_access_token = token_request.json()["access_token"]

    # Todo - I don't know what to do with the token, why does it have this message:
    # {'errors': [
    #     {'code': 32171, 'title': 'MANDATORY DATA MISSING', 'detail': "Missing mandatory query parameter 'keyword'",
    #      'source': {'parameter': 'keyword'}, 'status': 400}]}

    # header = {
    #     "Authorization": f"Bearer {amadeus_access_token}"
    # }
    #
    # city_data = {
    #     # "keyword": #NEEDS TO TAKE KEYWORD FROM SHEETY
    #     "keyword": "LONDON"
    # }
    # city_search_request = requests.get(url=AMADEUS_CITY_SEARCH_URL, headers=header, data=city_data)
    # print(city_search_request.json())