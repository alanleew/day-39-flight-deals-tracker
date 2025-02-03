# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from flight_data import FlightData
from data_manager import DataManager

# sheet_data = DataManager().json_data["prices"]
sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
              {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
              {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
              {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
              {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
              {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
              {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
              {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
              {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378},
              {'city': 'Taiwan', 'iataCode': '', 'id': 11, 'lowestPrice': 900}]
pprint(sheet_data)
