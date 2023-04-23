import unittest
from employee import Employee
import requests
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')
        #return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear down class')
        #return super().tearDownClass()

    def setUp(self) -> None:
        self.emp1 = Employee('shahar','lavon',1000)
        print('setup')
        #return super().setUp()
    def tearDown(self) -> None:
        print('teardown')
        # return super().tearDown()

    def test_email(self):
        
        self.assertEqual(self.emp1.email, 'shahar.lavon@gmail.com')
        print(self.emp1.email)

    def test_raise(self):
        
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.pay,1050)
        print(self.emp1.pay)

    def test_monthly_schedule(self):
        with patch('emloyee.requests.get') as mocked_get:
            mocked_get.return_value.ok



if __name__ == "__main__":
    unittest.main()
