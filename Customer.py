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
        dict_data = {'name': self.__name, 'last_name': self.__last_name, 'cc': self.__cc, 'age': self.__age,
               'tell': self.__tell, 'email': self.__email}
        return dict_data
