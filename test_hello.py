import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_uses_name(self):
        self.assertIn("World", greet("World"))


if __name__ == "__main__":
    unittest.main()
