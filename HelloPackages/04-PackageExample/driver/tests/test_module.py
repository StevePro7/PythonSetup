import unittest
#from src.module import getAge
from driver.src.module import getAge
from driver.src.module import getWgt

class TestMyFoo(unittest.TestCase):
    def test_lang(self):
        age = getAge()
        self.assertEqual(age, 10)
        
    def test_weight(self):
        wgt = getWgt()
        self.assertEqual(wgt, 80)
        

if __name__ == '__main__':
    unittest.main()
