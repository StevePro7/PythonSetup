"""Docstring1"""
import unittest
from MyPackage.src.module import add_one

class TestSimple(unittest.TestCase):

    """Docstring3"""
    def test_add_one(self):
        """Docstring3"""
        result = add_one(5)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
