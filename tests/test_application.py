import unittest
from tkinter import Tk
from gui.main_gui import MainGUI

class TestApplication(unittest.TestCase):
    def setUp(self):
        """Initialisiert ein Tkinter-Root-Objekt für jeden Test."""
        self.root = Tk()
        self.app = MainGUI(self.root)

    def tearDown(self):
        """Schließt das Tkinter-Root-Objekt nach jedem Test."""
        self.root.destroy()

    def test_copy_paste_functionality(self):
        """Testet die Copy-Paste-Funktion."""
        # Testcode hier
        pass

    def test_sorting_functionality(self):
        """Testet die Sortierung der Tabelle."""
        # Testcode hier
        pass

    def test_table_editing(self):
        """Testet das Bearbeiten und Speichern der Tabelle."""
        # Testcode hier
        pass

    def test_missing_json_handling(self):
        """Testet die Handhabung fehlender JSON-Datei."""
        # Testcode hier
        pass

    def test_debug_window(self):
        """Testet das Debug-Fenster."""
        # Testcode hier
        pass

if __name__ == '__main__':
    unittest.main()
