from Pet import Pet
from Servicio import Servicio
from Customer import Customer
from Veterinarian import Veterinarian
from Bill import Bill
from tabulate import tabulate

def request_info(menu):
    """Request info to add to the table.

    Args:
        menu (str): Menu that corresponds to the table to which the information is to be added.

    Returns:
        str: Table's name.
        dict: Dictionary with the information to be added.
    """
    if menu == 'cliente' or menu == 'veterinario':
        person = []
        # Request info to add to the table:
        person.append(input("Ingrese el nombre: "))
        person.append(input("Ingrese el apellido: "))
        person.append(input("Ingrese la cédula: "))
        person.append(input("Ingrese la edad: "))
        person.append(input("Ingrese el teléfono: "))
        person.append(input("Ingrese el correo electrónico: "))        
        
    if menu == 'cliente':
        # Create a new customer:
        customer = Customer(person[0], person[1], person[2], person[3], person[4], person[5])
        return 'customer', customer.add_customer()
    
    if menu == 'veterinario':
        veterinarian = person
        # Request info to add to the table:
        veterinarian.append(input("Ingrese la especialidad: "))
        veterinarian.append(input("Ingrese el salario: "))
        
        # Create a new veterinarian:
        veterinarian = Veterinarian(veterinarian[0], veterinarian[1], veterinarian[2], veterinarian[3],
                                    veterinarian[4], veterinarian[5], veterinarian[6], veterinarian[7])
        return 'veterinarian', veterinarian.add_veterinarian()
    
    if menu == 'mascota':
        mascota = []
        # Request info to add to the table:
        mascota.append(input("Ingrese el nombre: "))
        mascota.append(input("Ingrese la especie: "))
        mascota.append(input("Ingrese la edad: "))
        mascota.append(input("Ingrese la raza: "))
        mascota.append(input("Ingrese el color: "))
        mascota.append(input("Ingrese el peso: "))
        mascota.append(input("Ingrese el género: "))
        mascota.append(int(input("Ingrese el id del dueño: ")))
        
        # Create a new pet:
        pet = Pet(mascota[0], mascota[1], mascota[2], mascota[3], mascota[4], mascota[5], mascota[6], mascota[7])
        return 'pets', pet.register_pet()
    
    if menu == 'servicio':
        servi=[]
        # Request info to add to the table:
        servi.append(input("Ingrese la descripción: "))
        servi.append(int(input("Ingrese el precio: ")))
        servi.append(int(input("Ingrese el id del cliente: ")))
        servi.append(int(input("Ingrese el id del veterinario: ")))
        
        # Create a new service:
        service = Servicio(servi[0], servi[1], servi[2], servi[3])        
        return 'services', service.addServices()
    
def request_deletion_info(table):
    """Request info to delete from the table.

    Args:
        table (list): Table from which the information is to be deleted.

    Returns:
        str: id of the row to be deleted.
    """
    code_exists = False
    # Ask for the id to delete:
    delete_id = int(input("Ingrese el id que desea eliminar: "))
    for i in table:
        # Check if the id exists:
        if i[0] == delete_id:
            code_exists = True
            break
    if not code_exists:
        delete_id = ''
    
    return delete_id
            
def nameTable(menu):
    """Return the name of the table.
    
    Args:
        menu (str): Menu that corresponds to the table.
    
    Returns:
        str: Name of the table.
    """
    if menu == 'cliente':
        name_table = 'customer'
    elif menu == 'mascota':
        name_table = 'pets'
    elif menu == 'veterinario':
        name_table = 'veterinarian'
    else:
        name_table = 'services'
    
    return name_table

def showTable(listTable):
    """Display the table.

    Args:
        listTable (list): Table to be displayed.
    """
    print("\n" + tabulate(listTable[1:], headers=listTable[0]) + "\n")

def generate_bill(vet_name, cust_table, dict_register):
    """Generate a bill.

    Args:
        vet_name (str): Name of the veterinary.
        cust_table (list): Customer table.
        dict_register (dict): Dictionary with the service information.

    Returns:
        dict: Dictionary with the information to generate the bill.
    """
    # Get the customer's id:
    id_cust = dict_register['idCustomer']
    # Get the customer's name:
    cust_name = [row[1] for row in cust_table if row[0] == id_cust][0]
    
    # Create the bill:
    bill = Bill(vet_name, cust_name, dict_register['description_service'], dict_register['price'])
    return bill.generate_bill()

def update(menu):
    # Ask for the id to update:
    id = int(input("Ingrese el id que desea actualizar: "))
    
    if menu == 'cliente' or menu == 'veterinario':
        # Request info to update the table:
        person = []
        person.append(input("Ingrese el nuevo nombre: "))
        person.append(input("Ingrese el nuevo apellido: "))
        person.append(input("Ingrese la nueva cédula: "))
        person.append(input("Ingrese la nueva edad: "))
        person.append(input("Ingrese el nuevo teléfono: "))
        person.append(input("Ingrese el nuevo correo electrónico: "))        
        
    if menu == 'cliente':
        # Update the customer:
        customer = Customer(person[0], person[1], person[2], person[3], person[4], person[5])
        return customer.add_customer(), id
    
    if menu == 'veterinario':
        # Request info to update the table:
        veterinarian = person
        veterinarian.append(input("Ingrese la nueva especialidad: "))
        veterinarian.append(input("Ingrese el nuevo salario: "))
        
        # Update the veterinarian:
        veterinarian = Veterinarian(veterinarian[0], veterinarian[1], veterinarian[2], veterinarian[3],
                                    veterinarian[4], veterinarian[5], veterinarian[6], veterinarian[7])
        return veterinarian.add_veterinarian(), id
    
    if menu == 'mascota':
        # Request info to update the table:
        mascota = []
        mascota.append(input("Ingrese el nuevo nombre: "))
        mascota.append(input("Ingrese la nueva especie: "))
        mascota.append(input("Ingrese la nueva edad: "))
        mascota.append(input("Ingrese la nueva raza: "))
        mascota.append(input("Ingrese el nuevo color: "))
        mascota.append(input("Ingrese el nuevo peso: "))
        mascota.append(input("Ingrese el nuevo género: "))
        mascota.append(int(input("Ingrese el nuevo id del dueño: ")))
        
        # Update the pet:
        pet = Pet(mascota[0], mascota[1], mascota[2], mascota[3], mascota[4], mascota[5], mascota[6], mascota[7])
        return pet.register_pet(), id
    
    if menu == 'servicio':
        # Request info to update the table:
        servi=[]
        servi.append(input("Ingrese la nueva descripción: "))
        servi.append(int(input("Ingrese el nuevo precio: ")))
        servi.append(int(input("Ingrese el nuevo id del cliente: ")))
        servi.append(int(input("Ingrese el nuevo id del veterinario: ")))
        
        # Update the service:
        service = Servicio(servi[0], servi[1], servi[2], servi[3])        
        return service.addServices(), id
    