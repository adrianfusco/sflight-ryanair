import argparse

from search.validator import Validations


class Parser:
    """Class used to parse all the arguments
    provided by CLI and check the required ones
    """

    def __init__(self: object):
        parser_description = """
        Parse the information required to get information
        about flights in RyanAir
        """
        self.parser = argparse.ArgumentParser(
            description=parser_description
        )
        self.__add_new_arguments()
        self.arguments = self.parser.parse_args()

    def __add_new_arguments(self: object) -> None:
        self.parser.add_argument(
            '--departure-date',
            dest='departure_date',
            required=True,
            default=None,
            type=Validations.validate_date_input
        )
        self.parser.add_argument(
            '--origin',
            dest='origin',
            required=True
        )
        self.parser.add_argument(
            '--destination',
            dest='destination',
            required=True
        )
        self.parser.add_argument(
            '--only-arrivals',
            dest='only_arrivals',
            required=False,
            action=argparse.BooleanOptionalAction
        )
        self.parser.add_argument(
            '--only-departures',
            dest='only_departures',
            required=False,
            action=argparse.BooleanOptionalAction
        )

    def get_arguments(self: object):
        return self.arguments
