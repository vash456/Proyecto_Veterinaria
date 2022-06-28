from Pet import Pet
from Servicio import Servicio
from person import Customer, Veterinarian
from tabulate import tabulate

def request_info(menu):
    if menu == 'cliente' or menu == 'veterinario':
        person = []
        person.append(input("Ingrese el nombre: "))
        person.append(input("Ingrese el apellido: "))
        person.append(input("Ingrese la cédula: "))
        person.append(input("Ingrese la edad: "))
        person.append(input("Ingrese el teléfono: "))
        person.append(input("Ingrese el correo electrónico: "))        
        
    if menu == 'cliente':
        customer = Customer(person[0], person[1], person[2], person[3], person[4], person[5])
        return 'customer', customer.add_customer()
    
    if menu == 'veterinario':
        veterinarian = person
        veterinarian.append(input("Ingrese la especialidad: "))
        veterinarian.append(input("Ingrese el salario: "))
        
        veterinarian = Veterinarian(veterinarian[0], veterinarian[1], veterinarian[2], veterinarian[3],
                                    veterinarian[4], veterinarian[5], veterinarian[6], veterinarian[7])
        return 'veterinarian', veterinarian.add_veterinarian()
    
    if menu == 'mascota':
        mascota = []
        mascota.append(input("Ingrese el nombre: "))
        mascota.append(input("Ingrese la especie: "))
        mascota.append(input("Ingrese la edad: "))
        mascota.append(input("Ingrese la raza: "))
        mascota.append(input("Ingrese el color: "))
        mascota.append(input("Ingrese el peso: "))
        mascota.append(input("Ingrese el género: "))
        mascota.append(int(input("Ingrese el id del dueño: ")))
        
        pet = Pet(mascota[0], mascota[1], mascota[2], mascota[3], mascota[4], mascota[5], mascota[6], mascota[7])
        return 'pets', pet.register_pet()
    
    if menu == 'servicio':
        servi=[]
        servi.append(input("Ingrese la descripción: "))
        servi.append(int(input("Ingrese el precio: ")))
        servi.append(int(input("Ingrese el id del cliente: ")))
        servi.append(int(input("Ingrese el id del veterinario: ")))
        
        service = Servicio(servi[0], servi[1], servi[2], servi[3])        
        return 'services', service.addServices()
    
def request_deletion_info(menu):
    # Listar menu
    pass

def showTable(listTable):
    print("\n" + tabulate(listTable[1:], headers=listTable[0]) + "\n")