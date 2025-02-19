# Unit Testing - Calc
''' This module helps in testing modular functions alongside our testcases.'''

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self): # All test must start with 'test_'
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
 
    def test_subtract(self): # All test must start with 'test_'
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)
 
    def test_multiply(self): # All test must start with 'test_'
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)
 
    def test_divide(self): # All test must start with 'test_'
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertEqual(calc.divide(5,2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        # Alternatively using context manager:
        with self.assertRaises(ValueError):
            calc.divide(2, 0)



# This line is used to run our module
if __name__ == '__main__':
    unittest.main() # This will run all our test cases

''' Alternatively, To run our test case run the following command on terminal -
python -m unittest unit-testing.py'''