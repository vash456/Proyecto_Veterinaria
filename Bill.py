class Bill:
    def __init__(self, veterinary_name, customer_name, service, total):
        self._veterinary_name = veterinary_name
        self._customer_name = customer_name
        self._service = service
        self._total = total
        
    def generate_bill(self):
        dict_data = {'veterinary_name': self._veterinary_name, 'customer_name': self._customer_name,
                     'service': self._service, 'total': self._total}
        return dict_data
            