# Unit Testing - Employee
''' Testcase don't run in order. So keep tests isolated from one another.'''

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # Used to instantiate object once and use it across multiple testcases
    def setUp(self):
        print('\nSetUp called')
        self.emp1 = Employee('Tanishqua', 'Bansal', 50000)
        self.emp2 = Employee('Somilli', 'Dave', 60000)
    
    def tearDown(self):
        print('tearDown called')

    def test_email(self):
        print('test_email called')
        self.assertEqual(self.emp1.email, 'Tanishqua.Bansal@email.com')
        self.assertEqual(self.emp2.email, 'Somilli.Dave@email.com')

        self.emp1.first = 'Lamha'
        self.emp2.first = 'Yatri'

        self.assertEqual(self.emp1.email, 'Lamha.Bansal@email.com')
        self.assertEqual(self.emp2.email, 'Yatri.Dave@email.com')

    def test_fullname(self):
        print('test_fullname called')
        self.assertEqual(self.emp1.fullname, 'Tanishqua Bansal')
        self.assertEqual(self.emp2.fullname, 'Somilli Dave')

        self.emp1.first = 'Lamha'
        self.emp2.first = 'Yatri'

        self.assertEqual(self.emp1.fullname, 'Lamha Bansal')
        self.assertEqual(self.emp2.fullname, 'Yatri Dave')

    def test_apply_raise(self):
        print('test_apply_raise called')
        self.emp1.apply_raise()
        self.emp2.apply_raise()
    
        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

if __name__ == '__main__':
    unittest.main()

''' Resume Corey Schafer from 27:05 -> https://www.youtube.com/watch?v=6tNS--WetLI
Neural Nine -> https://www.youtube.com/watch?v=UL0opWf3DeM
Docs - https://docs.python.org/3/library/unittest.html#module-unittest'''