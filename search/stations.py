import requests

class Stations:
    """Class used to get all the available
    airports in RyanAir"""

    API_URL = 'https://www.ryanair.com/api/booking/v4/en-gb/res/stations'

    @staticmethod
    def get_stations():
        headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
        }
        stations = requests.get(
            Stations.API_URL,
            headers=headers
        ).json()
        return stations
