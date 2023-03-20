import unittest
from datetime import date

from model.battery.nubbin import Nubbin


class TestNubbin (unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-03-20")
        last_service_date = date.fromisoformat("2019-03-10")
        battery = Nubbin(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())



