"""Small sanity checks using Python's built-in unittest."""

import unittest

from main import greet


class TestGreeting(unittest.TestCase):
    def test_returns_text(self):
        self.assertIsInstance(greet("Developer"), str)

    def test_mentions_name(self):
        self.assertIn("Developer", greet("Developer"))

    def test_works_for_another_name(self):
        self.assertIn("Student", greet("Student"))


if __name__ == "__main__":
    unittest.main()
