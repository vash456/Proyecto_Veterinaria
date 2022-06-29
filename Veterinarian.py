from person import Person

class Veterinarian(Person):
    """Veterinary employee."""
    def __init__(self, name, last_name, cc, age, tell, email, speciality, salary):
        super().__init__(name, last_name, cc, age, tell, email)
        self.__speciality = speciality
        self.__salary = salary
        
    def add_veterinarian(self):
        """Create dictionary with veterinarian's information.

        Returns:
            dict: Dictionary with veterinarian's information.
        """
        dict_data = {'name': self.__name, 'last_name': self.__last_name, 'cc': self.__cc, 'age': self.__age,
               'tell': self.__tell, 'email': self.__email, 'speciality': self.__speciality, 'salary': self.__salary}
        return dict_data
    