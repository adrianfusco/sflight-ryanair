from sflight.requests import Request


class Stations:
    """Class used to get all the available
    airports in RyanAir"""

    API_URL = 'https://www.ryanair.com/api/booking/v4/en-gb/res/stations'

    @staticmethod
    def get_available_stations():
        return Request(url=Stations.API_URL).get_data_from_url()
