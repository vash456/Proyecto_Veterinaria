
class Servicio:
    def __init__(self, description, price, idCustomer, idVeterinarian):
        self._description = description
        self._price = price
        self._idCustomer = idCustomer
        self._idVeterinarian = idVeterinarian

    def addServices(self):
        dict_data = {'description': self._description, 'price': self._price, 'idCustomer': self._idCustomer,
                     'idVeterinarian': self._idVeterinarian}
        return dict_data
                