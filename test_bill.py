from Bill import Bill
import unittest

bill_test1 = Bill('Veterinaria Brothers', 'sasuke', 'peluqueria', 37000)
bill_test2 = Bill('Veterinaria Sisters', 'madara', 'vacuna', 23000)

class testBill(unittest.TestCase):
    def test_generate_bill(self):
        respuesta1 = bill_test1.generate_bill()
        dic_generado1 = {'veterinary_name': 'Veterinaria Brothers', 'customer_name': 'sasuke',
                     'service': 'peluqueria', 'total': 37000}
        self.assertDictEqual(dic_generado1,respuesta1)
        
        respuesta2 = bill_test2.generate_bill()
        dic_generado2 = {'veterinary_name': 'Veterinaria Sisters', 'customer_name': 'madara',
                     'service': 'vacuna', 'total': 23000}
        self.assertDictEqual(dic_generado2,respuesta2)
        
unittest.main(argv=[''],verbosity=2,exit=False)