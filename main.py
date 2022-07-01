import Historical
from connection import DAO
import functions

def main_menu():
    """Display the main menu."""
    continue_main = True
    # While the user wants to continue:
    while continue_main == True:
        right_option_main = False
        # While the user doesn't select a valid option:
        while not right_option_main:
            # Display the main menu:
            print("\n============= MENÚ PRINCIPAL =============")
            print("1. Clientes")
            print("2. Mascotas")
            print("3. Veterinarios")
            print("4. Servicios")
            print("5. Historial")
            print("6. Facturas")
            print("7. Ver información veterinaria")
            print("8. Salir")   
            print("==========================================\n")
            
            # Ask the user to enter an option:
            option_main = int(input("Seleccione una opción: "))
            
            # If the user selected an invalid option:
            if option_main < 1 or option_main > 8:
                # Display an error message:
                print("Opción incorrecta, ingrese nuevamente...")   
            elif option_main == 8:
                # Exit the program:
                continue_main = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                right_option_main = True
                # Execute the corresponding function:
                execute_option_main(option_main)

def execute_option_main(option_main):
    """Check selected option in the main menu
    and execute the corresponding function.

    Args:
        option_main (int): Option entered by the user.
    """
    if option_main == 1:
        try:
            menu = "cliente"
            # Display the client sub-menu:
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 2:
        try:
            menu = "mascota"
            # Display the pet sub-menu:
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 3:
        try:
            menu = "veterinario"
            # Display the veterinarian sub-menu:
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 4:
        try:
            menu = "servicio"
            # Display the service sub-menu:
            sub_menu(menu)        
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 5:
        try:
            # Display the history sub-menu:
            submenu_history()
        except:
            print("Ocurrió un error...")
    elif option_main == 6:
        try:
            # Display the bill table:
            display_bill()
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 7:
        try:
            # Display the veterinary information:
            display_vet_info()
        except Exception as ex:
            print("Ocurrió un error...", ex)
    else:
        # Display an error message:
        print("Opción no válida...")
        
def sub_menu(menu):
    """Display the corresponding sub-menu.

    Args:
        menu (str): Indicates the corresponding sub-menu.
    """
    continue_menu = True
    while continue_menu == True:
        right_option = False
        while not right_option:
            # Display the sub-menu:
            print("\n============= MENÚ {0}S =============".format(menu.upper()))
            print("1. Registrar {0}".format(menu))
            print("2. Actualizar {0}".format(menu))
            print("3. Eliminar {0}".format(menu))
            print("4. Listar {0}s".format(menu))
            print("5. Volver")
            print("==========================================\n")
            
            # Ask the user to enter an option:
            option = int(input("Seleccione una opción: "))

            # If the user selected an invalid option:
            if option < 1 or option > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 5:
                # Go back to the main menu:
                continue_menu = False
                break
            else:
                right_option = True
                # Execute the corresponding function:
                execute_option(option, menu)

def execute_option(option, menu):
    """Check selected option in the sub-menu
    and execute the corresponding function.

    Args:
        option (int): Option entered by the user.
        menu (str): Indicates the corresponding sub-menu.
    """
    # Create a DAO object:
    dao = DAO()
    
    if option == 1:
        # Request the user to enter the data:
        table_name, dict_register = functions.request_info(menu)
        # Insert the data in the table:
        dao.register(table_name, dict_register)
        if menu == 'servicio':
            # Get veterinary name:
            vet_name = dao.listTable('veterinary')[1][1]
            # Get Customer table:
            cust_table = dao.listTable('customer')
            # Generate a bill:
            dict_bill = functions.generate_bill(vet_name, cust_table, dict_register)
            # Insert the bill in the table:
            dao.register('bill', dict_bill)
    elif option == 2:
        # Get the table name:
        name_table = functions.nameTable(menu)
        # Get the corresponding table:
        table = dao.listTable(name_table)
        # Display the table:
        functions.showTable(table)
        # Request the user to enter the new data:
        dict_update, id = functions.update(menu)
        # Update the data in the table:
        dao.update(name_table, dict_update, id)
    elif option == 3:
        # Get the table name:
        name_table = functions.nameTable(menu)
        # Get the corresponding table:
        table = dao.listTable(name_table)
        # Display the table:
        functions.showTable(table)
        # Request the user to enter the data to delete:
        delete_id = functions.request_deletion_info(table)
        # If the user selected an existing id:
        if not(delete_id == ''):
            # Delete the data from the table:
            dao.delete(name_table, delete_id)
    elif option == 4:
        # Get the table name:
        name_table = functions.nameTable(menu)
        # Get the corresponding table:
        table = dao.listTable(name_table)
        # Display the table:
        functions.showTable(table)
    else:
        # Display an error message:
        print("Opción no válida...")
       
 
def submenu_history():
    """Display the history sub-menu."""
    continue_menu = True
    while continue_menu == True:
        right_option = False
        while not right_option:
            # Display history sub-menu:
            print("\n============= MENÚ HISTORIAL =============")
            print("1. Consultar historial por cliente ")
            print("2. Consultar historial por medico veterinario ")
            print("3. Volver")
            print("==========================================\n")
            
            # Ask the user to enter an option:
            option = int(input("Seleccione una opción: "))
        
            # If the user selected an invalid option:
            if option < 1 or option > 3:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 3:
                # Go back to the main menu:
                continue_menu = False
                break
            else:
                right_option = True
                if option == 1:
                    # Ask the user to enter the customer id:
                    id = int(input("Ingrese el id del cliente: "))
                    listHistorical = Historical.queryIdCustomer(id)
                    # Display the history:
                    functions.showTable(listHistorical)
                elif option == 2:
                    # Ask the user to enter the veterinarian id:
                    id = int(input("Ingrese el id del veterinario: "))
                    listHistorical = Historical.queryIdVeterinarian(id)
                    # Display the history:
                    functions.showTable(listHistorical)


def display_bill():
    """Display the bill table."""
    # Create a DAO object:
    dao = DAO()
    # Get the bill table:
    table = dao.listTable('bill')
    # Display the bill table:
    functions.showTable(table)

def display_vet_info():
    """Display the veterinary information."""
    # Create a DAO object:
    dao = DAO()
    # Get the veterinary table:
    table = dao.listTable('veterinary')
    # Display the veterinary table:
    functions.showTable(table)

main_menu() 
