import unittest
from driver.src.module import getAge

class TestMyFoo(unittest.TestCase):
    def test_lang(self):
        age = getAge()
        #age = 16
        self.assertEqual(age, 250)

if __name__ == '__main__':
    unittest.main()
