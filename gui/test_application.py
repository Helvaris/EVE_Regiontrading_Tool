import unittest
from utils import is_valid_number, calculate_value
from config import restore_window_position, save_window_position
import os
import json
import pyperclip

class TestApplication(unittest.TestCase):

    def test_is_valid_number(self):
        self.assertTrue(is_valid_number("1'000"))
        self.assertTrue(is_valid_number("1234.56"))
        self.assertFalse(is_valid_number("invalid"))
        self.assertFalse(is_valid_number("1'000a"))

    def test_calculate_value(self):
        thresholds = [
            {"ISK": 1.0, "Prozent": 75},
            {"ISK": 2000000.0, "Prozent": 70}
        ]
        self.assertEqual(calculate_value(100, thresholds), (175.0, 75))
        self.assertEqual(calculate_value(2000000, thresholds), (3400000.0, 70))
        self.assertEqual(calculate_value(0.5, thresholds), (0.5, 0))

    def test_config_save_restore(self):
        test_config = {
            "geometry": "800x600",
            "table_data": [{"ISK": 1000, "Prozent": 75}]
        }
        save_window_position(root=None, table_data=test_config)
        restored = restore_window_position(root=None)
        self.assertEqual(restored, test_config["table_data"])
        os.remove("config.json")

    def test_clipboard(self):
        pyperclip.copy("123")
        self.assertEqual(pyperclip.paste(), "123")
        pyperclip.copy("Test")
        self.assertEqual(pyperclip.paste(), "Test")

if __name__ == "__main__":
    unittest.main()
