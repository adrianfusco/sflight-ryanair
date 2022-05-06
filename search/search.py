from sys import exit

import requests
from tabulate import tabulate

from search.parser import Parser

API_URL = 'https://www.ryanair.com/api/booking/v4/es-es/availability'


def print_flight_info(flight_info: dict) -> None:
    flight_list_info = []
    for trip in flight_info['trips']:
        origin_city = trip['originName']
        destination_city = trip['destinationName']
        for trip_date in trip['dates']:
            if not trip_date['flights']:
                print(
                    f"Not flights available for day {trip_date['dateOut']}\n"
                )
                continue
            for flight in trip_date['flights']:
                if flight['faresLeft'] == 0:
                    continue
                amount = flight['regularFare']['fares'][0]['amount']
                flight_list_info.append(
                    [
                        origin_city,
                        destination_city,
                        flight['flightNumber'],
                        f"{flight['duration']}h",
                        ' -> '.join(flight['time']),
                        f"{amount} {flight_info['currency']}",
                    ]
                )
    print(
        tabulate(
            flight_list_info,
            headers=[
                'Origin City',
                'Destination City',
                'Flight number',
                'Flying duration',
                'Time departure -> Time arrival',
                'Price'
            ]
        )
    )


def main():
    parser = Parser()
    arguments = parser.get_arguments()
    payload = {
        'DateIn': arguments.departure_date,
        'DateOut': arguments.departure_date,
        'Origin': arguments.origin,
        'Destination': arguments.destination,
        'ToUs': 'AGREED',
        'IncludeConnectingFlights': 'false',
        'FlexDaysBeforeIn': 0,
        'FlexDaysIn': 0,
        'FlexDaysBeforeOut': 0,
        'FlexDaysOut': 0,
        'RoundTrip': 'true',
        'ChangeFlight': 'undefined',
        'Disc': 0,
        'INF': 0,
        'TEEN': 0,
        'CHD': 0,
        'ADT': 1
    }
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }
    flight_info = requests.get(
        API_URL,
        params=payload,
        headers=headers
    ).json()

    if 'trips' not in flight_info:
        print(flight_info['message'])
        exit(1)

    print_flight_info(flight_info)


if __name__ == "__main__":
    main()
