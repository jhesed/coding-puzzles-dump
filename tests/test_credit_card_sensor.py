import unittest

from src.credit_card_sensor import censor


class TestCreditCardSensor(unittest.TestCase):
    def test_ControlStructures___normal_16_digit_cards(self):
        self.assertEqual(censor("1244 5005 3701 9993"), "xxxx xxxx xxxx 9993")

    def test_ControlStructures___rare_18_digit_cards(self):
        self.assertEqual(censor("67619600 0000551045"), "xxxxxxxx xxxxxx1045")

    def test_ErrorHandling___letters_in_card_Numbers(self):
        self.assertIsNone(censor("2A44 9891 EEEE FFFF"))
