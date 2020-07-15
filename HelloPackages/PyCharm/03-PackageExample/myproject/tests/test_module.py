import unittest
# from project.src.module import getAge
#from module import getAge
from src.module import getAge

class TestMyFoo(unittest.TestCase):
    def test_lang(self):
        age = getAge()
        #age = 16
        self.assertEqual(age, 18)

if __name__ == '__main__':
    unittest.main()
