""" Unit test module """
import unittest
from MyPackage.src.module import add_one

class TestSimple(unittest.TestCase):

    """ Unit Test class """
    def test_add_one(self):
        """ Test increment function """
        result = add_one(5)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
