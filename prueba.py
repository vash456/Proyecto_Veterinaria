from Servicio import Servicio
from connection import DAO


dao = DAO()

# consultar registros de la tabla
customers = dao.listTable("customer")
for customer in customers:
    print(customer)

# insertar registro nuevo en la tabla
# customer = []
# customer.append(input("ingrese name: "))
# customer.append(input("ingrese last_name: "))
# customer.append(input("ingrese CC: "))
# customer.append(input("ingrese age: "))
# customer.append(input("ingrese tell: "))
# customer.append(input("ingrese email: "))

# customer = []
# customer.append("julio")
# customer.append("perez")
# customer.append("5465987")
# customer.append("32")
# customer.append("216564")
# customer.append("correo123245@gmail.com")

# sql = """INSERT INTO customer (name, last_name, cc, age, tell, email) 
# VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');"""

# dao.registerData(customer, sql)

# servicio = Servicio("corte de pelo", 10000, 2, "123456")
# servicio.addServices()

# editar registro de customer
# customer = []
# customer.append(input("ingrese name: "))
# customer.append(input("ingrese last_name: "))
# customer.append(input("ingrese CC: "))
# customer.append(input("ingrese age: "))
# customer.append(input("ingrese tell: "))
# customer.append(input("ingrese email: "))
# customer.append(input("ingrese el idcustomer: "))
# dao.actualizarCustomer(customer)

# eliminar registros
# idCustomer = input("ingrese id customer a eliminar: ")
# dao.eliminarCustomer(idCustomer)