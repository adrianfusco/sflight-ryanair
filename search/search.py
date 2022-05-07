from sys import exit

import requests
from tabulate import tabulate
from search.exceptions import ArrivalsAndDeparturesAnulation

from search.parser import Parser

API_URL = 'https://www.ryanair.com/api/booking/v4/es-es/availability'


def print_flight_info(flight_info: dict, args) -> None:
    flight_list_info = []
    for trip in flight_info['trips']:
        origin_city = trip['originName']
        destination_city = trip['destinationName']

        if args.only_arrivals and \
            trip['destination'] == args.destination:
                continue

        if args.only_departures and \
            trip['origin'] == args.destination:
                continue

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
                        flight['time'][0],
                        flight['time'][1],
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
                'Time departure',
                'Time arrival',
                'Price'
            ]
        )
    )


def main():
    parser = Parser()
    args = parser.get_arguments()

    if args.only_arrivals and args.only_departures:
        raise ArrivalsAndDeparturesAnulation

    payload = {
        'DateIn': args.departure_date,
        'DateOut': args.departure_date,
        'Origin': args.origin,
        'Destination': args.destination,
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

    print_flight_info(flight_info, args)


if __name__ == "__main__":
    main()
