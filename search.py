from sys import exit
import requests
from search.parser import Parser

API_URL = 'https://www.ryanair.com/api/booking/v4/es-es/availability'


def print_flight_info(flight_info: dict) -> None:
    for trip in flight_info['trips']:
        origin_city = trip['originName']
        destination_city = trip['destinationName']
        print(
                f"\nOrigin: {origin_city}",
                "\n"
                f"Destination: {destination_city}",
                "\n\n"
            )
        for trip_date in trip['dates']:
            if not trip_date['flights']:
                print(
                    f"Not flights available for day {trip_date['dateOut']}\n"
                )
                continue
            print(
                f"{len(trip_date['flights'])}",
                f"flights available for day: {trip_date['dateOut']}\n"
            )
            for flight in trip_date['flights']:
                if flight['faresLeft'] == 0:
                    continue
                print(
                    f"  Flight Number: {flight['flightNumber']}\n",
                    f" Duration: {flight['duration']}h"
                )
                print("  Time UTC: ", *flight['time'], sep=" -> ")
                for price in flight['regularFare']['fares']:
                    print(
                        f"  Price: {price['amount']} ",
                        f"{flight_info['currency']}\n"
                    )
            print(
                "_" * 2 * max(
                    len(origin_city),
                    len(destination_city)
                ),
                end="\n"
            )


if __name__ == "__main__":
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
