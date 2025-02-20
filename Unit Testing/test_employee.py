# Unit Testing - Employee
''' Some best practices for Unit Testing -
1. Testcase don't run in order. So keep tests isolated from one another.
2. Test-driven development - You make testcases first and then start coding.
3. Any test is better than no test.

pytest is an alternative for unittest '''

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    # This will be called only once, at the beginning of the testing.
    @classmethod
    def setUpClass(self):
        print('\nSetUpClass called')
    
    @classmethod
    def tearDownClass(self):
        print('\ntearDownClass called')

    # Used to instantiate object once and use it across multiple testcases
    # It sets up everytime new testcase is ran.
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

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('September')
            mocked_get.assert_called_with('http://company.com/Bansal/September')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('December')
            mocked_get.assert_called_with('http://company.com/Dave/December')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()