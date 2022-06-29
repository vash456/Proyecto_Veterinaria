from person import Person

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
