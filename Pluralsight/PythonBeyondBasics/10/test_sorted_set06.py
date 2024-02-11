import unittest
from sorted_set import SortedSet


class TestReprProtocol(unittest.TestCase):

    def test_rep_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_some(self):
        s = SortedSet([42, 40, 19])
        expect: str = "SortedSet([19, 40, 42])"
        actual: str = repr(s)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()