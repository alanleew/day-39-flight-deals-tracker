# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from flight_data import FlightData
from data_manager import DataManager

dm = DataManager()
pprint(dm.sheet_data)
