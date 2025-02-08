# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
dm = DataManager()

from flight_search import FlightSearch
fs= FlightSearch()

sheet_data = dm.get_data()

for row in sheet_data:
    fs.search(row)
    dm.update_sheet(row)

# from pprint import pprint
# pprint(sheet_data)
