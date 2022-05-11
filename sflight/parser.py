import argparse

from sflight.validator import Validations


class Parser:
    """Class used to parse all the arguments
    provided by CLI and check the required ones
    """

    def __init__(self: object) -> None:
        parser_description = """
        Parse the information required to get information
        about flights and airports in RyanAir
        """
        self.parser = argparse.ArgumentParser(
            description=parser_description,
            prog='sflight'
        )

        self.subparsers = self.parser.add_subparsers()

        self.flights_parser = self.subparsers.add_parser(
            'flights',
            help='Get information between two flights'
        )
        self.airports_parser = self.subparsers.add_parser(
            'airports',
            help='Get information about airports'
        )

        self.__add_flights_arguments()
        self.__add_airports_arguments()

        self.arguments = self.parser.parse_args()

        if not len(vars(self.arguments)):
            self.parser.print_help()
            exit(1)

    def __add_flights_arguments(self: object) -> None:
        self.flights_parser.add_argument(
            '--departure-date',
            dest='departure_date',
            required=True,
            default=None,
            type=Validations.validate_date_input
        )
        self.flights_parser.add_argument(
            '--origin',
            dest='origin',
            required=True
        )
        self.flights_parser.add_argument(
            '--destination',
            dest='destination',
            required=True
        )
        self.flights_parser.add_argument(
            '--only-arrivals',
            dest='only_arrivals',
            required=False,
            action=argparse.BooleanOptionalAction
        )
        self.flights_parser.add_argument(
            '--only-departures',
            dest='only_departures',
            required=False,
            action=argparse.BooleanOptionalAction
        )
        self.flights_parser.add_argument(
            '--get-stations',
            dest='stations_requested',
            required=False,
            action=argparse.BooleanOptionalAction
        )

    def __add_airports_arguments(self: object) -> None:
        self.airports_parser.add_argument(
            '--get-stations',
            dest='stations_requested',
            required=False,
            action=argparse.BooleanOptionalAction
        )

    def get_arguments(self: object) -> argparse.ArgumentParser:
        return self.arguments
