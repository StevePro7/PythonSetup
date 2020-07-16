import unittest
from MyPackage.src.module import add_one

class TestSimple(unittest.TestCase):

    def test_add_one(self):
        result = add_one(5)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
