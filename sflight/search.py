from sys import exit

from tabulate import tabulate

from sflight.exceptions import (AirportNotAvailable,
                                ArrivalsAndDeparturesAnulation)
from sflight.parser import Parser
from sflight.requests import Request
from sflight.stations import Stations

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


def main() -> None:
    parser = Parser()
    args = parser.get_arguments()

    available_stations = Stations.get_available_stations()

    available_airports = "\nAvailable airports:\n" + \
        "\n".join(f"{airport_code, airport_info['name']}"
                  for airport_code, airport_info
                  in available_stations.items())

    if args.stations_requested:
        print(available_airports)
        exit(0)

    if args.origin not in available_stations.keys() or \
            args.destination not in available_stations.keys():
        raise AirportNotAvailable(available_airports)

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

    flight_info = Request(
        url=API_URL,
        payload=payload
    ).get_data_from_url()

    if 'trips' not in flight_info:
        print(flight_info['message'])
        exit(1)

    print_flight_info(flight_info, args)


if __name__ == "__main__":
    main()
