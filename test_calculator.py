from calculator import Calculator
import unittest
class testSumFromNumbers(unittest.TestCase):
    def test_sumFromNumbers(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        self.assertEqual(result,5)
        self.assertNotEqual(result,5)
        self.assertGreaterEqual(result,5)
        
    

unittest.main()