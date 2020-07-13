import unittest
from example_pkg import stackoverflow


class TestStackoverflow(unittest.TestCase):
    def test_lang(self):
        age = stackoverflow.hello()
        self.assertEqual(age, 28)


if __name__ == '__main__':
    unittest.main()
