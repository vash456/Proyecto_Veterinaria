from connection import DAO


dao = DAO()

# consultar registros de la tabla
customers = dao.listCustomers()
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
# dao.registerCustomer(customer)

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
# dao.eliminarCustomer()