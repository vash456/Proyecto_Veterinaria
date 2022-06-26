class Veterinaria:
    def __init__(self, name, nit, email, telephono, address):
        self.name = name
        self.nit = nit 
        self.email = email
        self.telephono = telephono
        self.address = address
        self.list_history = []
        self.list_customer = []

    def atender_cliente(self, Customer):
        pass
        
    def facturar(self, Servicio, Customer):
        pass

    def add_historial(self, History):
        self.list_history.append(History)