
from Customer import Customer
import unittest

class TestCustomer(unittest.TestCase):
    
        def test_add_customer(self):
            customer1 = Customer('Pablo', 'Muñoz', '123456789', '25', '3456789876', 'pablo@gmail.com')
            dict1 = {'name': 'Pablo', 'last_name': 'Muñoz', 'cc': '123456789', 'age': '25',
                  'tell': '3456789876', 'email': 'pablo@gmail.com'}
            customer2 = Customer('Camila', 'Acevedo', '1025987456', '30', '3226987451', 'camila@gmail.com')
            dict2 = {'name': 'Camila', 'last_name': 'Acevedo', 'cc': '1025987456', 'age': '30',
                  'tell': '3226987451', 'email': 'camila@gmail.com'}
            self.assertDictEqual(customer1.add_customer(), dict1)
            self.assertDictEqual(customer2.add_customer(), dict2)

unittest.main(argv=[''],verbosity=2, exit=False)
