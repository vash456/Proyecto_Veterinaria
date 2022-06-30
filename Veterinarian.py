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
        dict_data = {'name': self._Person__name, 'last_name': self._Person__last_name, 'cc': self._Person__cc,
                     'age': self._Person__age, 'tell': self._Person__tell, 'email': self._Person__email,
                     'speciality': self._Veterinarian__speciality, 'salary': self._Veterinarian__salary}
        return dict_data
    