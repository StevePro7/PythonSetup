import unittest


def my_generator(n):
    for i in range(n):
        yield i * 2


class TestGenerator(unittest.TestCase):
    def test_my_generator(self):
        # Initialize the generator
        gen = my_generator(5)

        # Use next() to get values from the generator
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 4)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 8)

        # Ensure StopIteration is raised after the last item
        with self.assertRaises(StopIteration):
            next(gen)

    def test_my_generator_all_values(self):
        # This test checks all yielded values in one go.
        gen = my_generator(5)

        values = list(gen)  # Collect all values from the generator

        self.assertEqual(values, [0, 2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()