from Pet import Pet
import unittest

pet_test1 = Pet('Toby', 'Perro', '3', 'Samoyedo', 'Blanco', '30', 'macho', 1)
pet_test2 = Pet('bruno', 'conejo', '1', 'gigante', 'gris', '5', 'macho', 3)

class testPet(unittest.TestCase):
    
    def test_register_pet(self):
        respuesta = pet_test1.register_pet()
        self.assertDictEqual(respuesta,{'name': 'Toby', 'species': 'Perro', 'age': '3', 'race': 'Samoyedo', 'color': 'Blanco', 'weight': '30', 'gender': 'macho', 'customer_idCustomer': 1})
        
        respuesta = pet_test2.register_pet()
        self.assertDictEqual(respuesta,{'name': 'bruno', 'species': 'conejo', 'age': '1', 'race': 'gigante', 'color': 'gris', 'weight': '5', 'gender': 'macho', 'customer_idCustomer': 3})
        
unittest.main(argv=[''],verbosity=2, exit=False)