import unittest
from project.src.module import getAge

class TestMyFoo(unittest.TestCase):
    def test_lang(self):
        age = getAge()
        self.assertEqual(age, 15)

if __name__ == '__main__':
    unittest.main()
