import unittest
from sorted_set import SortedSet


class TestOperationsSetProtocol(unittest.TestCase):

    def test_intersection(self):
        s = SortedSet((1, 2, 3))
        t = SortedSet((2, 3, 4))
        self.assertEqual(s & t, SortedSet({2, 3}))

    def test_union(self):
        s = SortedSet((1, 2, 3))
        t = SortedSet((2, 3, 4))
        self.assertEqual(s | t, SortedSet({1, 2, 3, 4}))

    def test_symmetric_difference(self):
        s = SortedSet((1, 2, 3))
        t = SortedSet((2, 3, 4))
        self.assertEqual(s ^ t, SortedSet({1, 4}))

    def test_difference(self):
        s = SortedSet((1, 2, 3))
        t = SortedSet((2, 3, 4))
        expect = SortedSet({1})
        actual = s - t
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()