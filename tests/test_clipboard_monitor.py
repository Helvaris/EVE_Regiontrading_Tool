import unittest
from unittest.mock import patch, MagicMock
from clipboard_monitor import monitor_clipboard
import pyperclip
import time

class TestClipboardMonitorWithTable(unittest.TestCase):
    def setUp(self):
        self.sample_thresholds = [
            {"ISK": 1.0, "Prozent": 75},
            {"ISK": 1000.0, "Prozent": 50},
        ]
        self.debug_var = MagicMock()
        self.input_label = MagicMock()
        self.output_label = MagicMock()
        self.threshold_label = MagicMock()
        self.active_tab = MagicMock()
        self.append_debug_log = MagicMock()
        self.root = MagicMock()

    @patch('clipboard_monitor.pyperclip.paste')
    @patch('clipboard_monitor.pyperclip.copy')
    def test_clipboard_with_dynamic_thresholds(self, mock_copy, mock_paste):
        """
        Testet, ob das Clipboard korrekt überwacht wird und die Berechnungen mit
        dynamischen Schwellenwerten durchgeführt werden.
        """
        mock_paste.side_effect = ["100", "500", "1500", "STOP"]
        mock_copy.side_effect = MagicMock()

        with patch('clipboard_monitor.sleep', return_value=None):
            start_time = time.time()
            monitor_clipboard(
                thresholds=self.sample_thresholds,
                debug_var=self.debug_var,
                input_label=self.input_label,
                output_label=self.output_label,
                threshold_label=self.threshold_label,
                active_tab=self.active_tab,
                append_debug_log=self.append_debug_log,
                root=self.root
            )
            elapsed_time = time.time() - start_time

            # Validate clipboard interactions
            self.assertTrue(mock_paste.called)
            self.assertTrue(mock_copy.called)

            # Check label updates
            self.input_label.config.assert_called()
            self.output_label.config.assert_called()
            self.threshold_label.config.assert_called()

            # Validate time constraints (test shouldn't run forever)
            self.assertLess(elapsed_time, 10)  # Test should complete in <10 seconds

if __name__ == "__main__":
    unittest.main()
