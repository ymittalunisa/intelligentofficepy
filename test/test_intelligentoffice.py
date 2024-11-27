import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError


class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass

    @patch.object(GPIO, "input")
    def test_check_quadrant_occupancy(self, mock_infra_pin1: Mock, mock_infra_pin2: Mock, mock_infra_pin3: Mock, mock_infra_pin4: Mock):
        mock_infra_pin1.return_value = True
        mock_infra_pin2.return_value = True
        mock_infra_pin3.return_value = True
        mock_infra_pin4.return_value = True
        inteloffice = IntelligentOffice()
        self.assertFalse(inteloffice.check_quadrant_occupancy(mock_infra_pin1))