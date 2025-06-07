import unittest
from collections.abc import Iterable
from sorted_set import SortedSet


class TestIterableProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.s: SortedSet = SortedSet([7, 2, 1, 1, 9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index: int = 0
        expected: list = [1, 2, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


if __name__ == '__main__':
    unittest.main()
