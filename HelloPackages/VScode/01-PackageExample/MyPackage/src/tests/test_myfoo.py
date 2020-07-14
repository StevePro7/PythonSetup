import unittest
#from MyPackage.MyFoo import MyBar
#import MyFoo
from tests.MyFoo import * 

class TestMyFoo(unittest.TestCase):
    def test_lang(self):
        bar = MyBar()
        age = bar.getAge()
        self.assertEqual(age, 9)

if __name__ == '__main__':
    unittest.main()
