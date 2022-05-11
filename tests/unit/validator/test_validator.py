from argparse import ArgumentTypeError
from datetime import datetime
from unittest import TestCase

from sflight.validator import Validations


class TestValidator(TestCase):

    def test_validate_date_input(self: object):
        validator = Validations()

        with self.assertRaises(ArgumentTypeError):
            validator.validate_date_input('2022-02-022')

        datetime_object = validator.validate_date_input('2022-02-02')
        self.assertTrue(type(datetime_object) is datetime)
