from person import Person

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
    