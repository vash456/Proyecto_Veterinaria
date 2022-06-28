class Person:
    """Class Person. Could be customer or veterinarian."""
    def __init__(self, name, last_name, cc, age, tell, email):
        self.name = name
        self.last_name = last_name
        self.cc = cc
        self.age = age
        self.tell = tell
        self.email = email
    
    # # To get name:    
    # def getName(self):
    #     return self.name
    
class Customer(Person):
    """Veterinary client. Pet's owner."""
    def __init__(self, name, last_name, cc, age, tell, email):
        super().__init__(name, last_name, cc, age, tell, email)
        
    def add_customer(self):
        """Create dictionary with customer's information.

        Returns:
            dict: Dictionary with customer's information.
        """
        dict_data = {'name': self.name, 'last_name': self.last_name, 'cc': self.cc, 'age': self.age,
               'tell': self.tell, 'email': self.email}
        return dict_data

class Veterinarian(Person):
    """Veterinary employee."""
    def __init__(self, name, last_name, cc, age, tell, email, speciality, salary):
        super().__init__(name, last_name, cc, age, tell, email)
        self.speciality = speciality
        self.salary = salary
        
    def add_veterinarian(self):
        """Create dictionary with veterinarian's information.

        Returns:
            dict: Dictionary with veterinarian's information.
        """
        dict_data = {'name': self.name, 'last_name': self.last_name, 'cc': self.cc, 'age': self.age,
               'tell': self.tell, 'email': self.email, 'speciality': self.speciality, 'salary': self.salary}
        return dict_data
    
    # def give_diagnosis(pet):
    #     pass             
        
    # def operate(pet, diagnosis):
    #     pass
    
  