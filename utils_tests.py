import unittest
from utils import utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.u = utils()

    # --- reversed tests ---
    def test_reversed_integer(self):
        self.assertEqual(self.u.reversed(1234), 4321)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            self.u.reversed("1234")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            self.u.reversed(12.34)

    # --- formatter tests ---
    def test_formatter_integer(self):
        self.assertEqual(self.u.formatter(8), ("1000", "10"))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            self.u.formatter("8")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            self.u.formatter(8.5)

if __name__ == "__main__":
    unittest.main()
