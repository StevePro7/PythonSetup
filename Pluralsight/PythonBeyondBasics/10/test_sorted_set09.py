import unittest
from sorted_set import SortedSet


class TestRelationalSetProtocol(unittest.TestCase):

    def test_lt_positive(self):
        s = SortedSet([1, 2])
        t = SortedSet([1, 2, 3])
        self.assertTrue(s < t)

    def test_lt_negative(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2, 3])
        self.assertFalse(s < t)

    def test_le_lt_positive(self):
        s = SortedSet([1, 2])
        t = SortedSet([1, 2, 3])
        self.assertTrue(s <= t)

    def test_le_eq_positive(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2, 3])
        self.assertTrue(s <= t)

    def test_le_negative(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2])
        self.assertFalse(s <= t)

    def test_gt_positive(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2])
        self.assertTrue(s > t)

    def test_gt_negative(self):
        s = SortedSet([1, 2])
        t = SortedSet([1, 2, 3])
        self.assertFalse(s > t)

    def test_ge_qt_positive(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2])
        self.assertTrue(s > t)

    def test_ge_eq_positive(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([1, 2, 3])
        self.assertTrue(s >= t)

    def test_ge_negative(self):
        s = SortedSet([1, 2])
        t = SortedSet([1, 2, 3])
        self.assertFalse(s >= t)


if __name__ == '__main__':
    unittest.main()
