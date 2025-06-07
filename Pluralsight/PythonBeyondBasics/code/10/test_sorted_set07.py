import unittest
from sorted_set import SortedSet


class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(SortedSet([4, 5, 6]) == SortedSet([6, 5, 4]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([4, 5, 6]) == SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([4, 5, 6]) == SortedSet([4, 5, 6]))

    def test_identical(self):
        s = SortedSet([10, 11, 12])
        self.assertTrue(s == s)


if __name__ == '__main__':
    unittest.main()
