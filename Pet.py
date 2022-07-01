
class Pet:
    def __init__(self, name, species, age, race, color, weight, gender,idCustomer):
        self.__name = name 
        self.__species = species 
        self.__age = age 
        self.__race = race 
        self.__color = color 
        self.__weight = weight 
        self.__gender = gender 
        self.__idCustomer = idCustomer
        
    def register_pet(self):        
        dic= {'name': self.__name, 'species': self.__species, 'age': self.__age, 'race': self.__race, 'color': self.__color,
              'weight': self.__weight, 'gender': self.__gender, 'customer_idCustomer': self.__idCustomer}
        
        return(dic)
    
    