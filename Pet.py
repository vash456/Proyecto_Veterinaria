
class Pet:
    def __init__(self, name, species, age, race, color, weight, gender,idCustomer):
        self._name = name 
        self._species = species 
        self._age = age 
        self._race = race 
        self._color = color 
        self._weight = weight 
        self._gender = gender 
        self._idCustomer=idCustomer
        
    def register_pet(self):
        dic= {'name': self._name, 'species': self._species, 'age': self._age, 'race': self._race, 'color': self._color,
              'weight': self._weight, 'gender': self._gender, 'customer_idCustomer': self._idCustomer}
        
        return(dic)
    
    