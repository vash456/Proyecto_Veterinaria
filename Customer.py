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
        dict_data = {'name': self._Person__name, 'last_name': self._Person__last_name, 'cc': self._Person__cc,
                     'age': self._Person__age, 'tell': self._Person__tell, 'email': self._Person__email}
        return dict_data
