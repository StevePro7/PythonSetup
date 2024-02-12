import unittest
from sorted_set import SortedSet


class TestContainerProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_container(self):
        self.assertTrue(7 in self.s)

    def test_negative_container(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)


if __name__ == '__main__':
    unittest.main()
