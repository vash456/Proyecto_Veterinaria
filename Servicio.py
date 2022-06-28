from connection import DAO


class Servicio:
    def __init__(self, description, price, idCustomer, dni_veterinarian):
        self.description = description
        self.price = price
        self.idCustomer = idCustomer
        self.dni_veterinarian = dni_veterinarian

    def addServices(self):
        sql = """INSERT INTO services (description, price, idCustomer, DNI_veterinarian) 
        VALUES ('{0}', {1}, {2}, {3});"""
        dao = DAO()
        data = []
        data.append(self.description)
        data.append(self.price)
        data.append(self.idCustomer)
        data.append(self.dni_veterinarian)

        dao.registerData(data, sql)
        
    def tableServices(self):
        dao = DAO()
        return dao.listTable("services")