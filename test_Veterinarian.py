
from Veterinarian import Veterinarian
import unittest

class TestCustomer(unittest.TestCase):
    
        def test_add_veterinarian(self):
            veterinarian1 = Veterinarian('Pablo', 'Muñoz', '123456789', '25', '3456789876', 'pablo@gmail.com',
                                         'Cirujano', '$5.000')
            dict1 = {'name': 'Pablo', 'last_name': 'Muñoz', 'cc': '123456789', 'age': '25', 'tell': '3456789876',
                     'email': 'pablo@gmail.com', 'speciality': 'Cirujano', 'salary': '$5.000'}
            veterinarian2 = Veterinarian('Camila', 'Acevedo', '1025987456', '30', '3226987451', 'camila@gmail.com',
                                         'Odontóloga', '$3.000')
            dict2 = {'name': 'Camila', 'last_name': 'Acevedo', 'cc': '1025987456', 'age': '30', 'tell': '3226987451', 
                     'email': 'camila@gmail.com',  'speciality': 'Odontóloga', 'salary': '$3.000'}
            self.assertDictEqual(veterinarian1.add_veterinarian(), dict1)
            self.assertDictEqual(veterinarian2.add_veterinarian(), dict2)

unittest.main(argv=[''],verbosity=2, exit=False)