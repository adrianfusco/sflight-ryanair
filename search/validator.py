from datetime import datetime
from argparse import ArgumentTypeError


class Validations:
    """Class used to validate all the inputs"""

    @staticmethod
    def validate_date_input(date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ArgumentTypeError(
                f"Date {date_str} not valid. Expected: 'YYYY-MM-DD'"
            )
