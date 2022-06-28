def request_info(menu):
    if menu == 'cliente' or menu == 'veterinario':
        name = input("Ingrese el nombre: ")
        last_name = input("Ingrese el apellido: ")
        cc = input("Ingrese la cédula: ")
        age = input("Ingrese la edad: ")
        tell = input("Ingrese el teléfono: ")
        email = input("Ingrese el correo electrónico: ")
    if menu == 'cliente':
        table = 'customer'
        customer = {'name': name, 'last_name': last_name, 'cc': cc, 'age': age, 'tell': tell, 'email': email}
        return table, customer
    if menu == 'veterinario':
        speciality = input("Ingrese la especialidad: ")
        salary = input("Ingrese el salario: ")
        table = 'veterinarian'
        veterinarian = {'name': name, 'last_name': last_name, 'cc': cc, 'age': age, 'tell': tell, 'email': email, 
                        'speciality': speciality, 'salary': salary}
        return table, veterinarian
    if menu == 'mascota':
        name = input("Ingrese el nombre: ")
        species = input("Ingrese la especie: ")
        age = input("Ingrese la edad: ")
        race = input("Ingrese la raza: ")
        color = input("Ingrese el color: ")
        weight = input("Ingrese el peso: ")
        gender = input("Ingrese el género: ")
        owner = int(input("Ingrese el id del dueño: "))
        table = 'pets'
        pet = {'name': name, 'species': species, 'age': age, 'race': race, 'color': color, 'weight': weight,
               'gender': gender, 'customer_idCustomer': owner}
        return table, pet
    if menu == 'servicio':
        description = input("Ingrese la descripción: ")
        price = int(input("Ingrese el precio: "))
        idCustomer = int("Ingrese el id del cliente: ")
        idVeterinarian = input("Ingrese el id del veterinario: ")
        table = 'services'
        service = {'description': description, 'price': price, 'idCustomer': idCustomer,
                   'idVeterinarian': idVeterinarian}
        return table, service
        