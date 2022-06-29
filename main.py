from connection import DAO
import functions

def main_menu():
    """Display the main menu."""
    continue_main = True
    while continue_main == True:
        right_option_main = False
        while not right_option_main:
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
            
            option_main = int(input("Seleccione una opción: "))
            
            if option_main < 1 or option_main > 8:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option_main == 8:
                continue_main = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                right_option_main = True
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
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 2:
        try:
            menu = "mascota"
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 3:
        try:
            menu = "veterinario"
            sub_menu(menu)
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 4:
        try:
            menu = "servicio"
            sub_menu(menu)        
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 5:
        try:
            display_history()
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 6:
        try:
            display_bill()
        except Exception as ex:
            print("Ocurrió un error...", ex)
    elif option_main == 7:
        try:
            display_vet_info()
        except Exception as ex:
            print("Ocurrió un error...", ex)
    else:
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
            print("\n============= MENÚ {0}S =============".format(menu.upper()))
            print("1. Registrar {0}".format(menu))
            print("2. Actualizar {0}".format(menu))
            print("3. Eliminar {0}".format(menu))
            print("4. Listar {0}s".format(menu))
            print("5. Voler")
            print("==========================================\n")
            
            option = int(input("Seleccione una opción: "))
        
            if option < 1 or option > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 5:
                continue_menu = False
                break
            else:
                right_option = True
                execute_option(option, menu)

def execute_option(option, menu):
    """Check selected option in the sub-menu
    and execute the corresponding function.

    Args:
        option (int): Option entered by the user.
        menu (str): Indicates the corresponding sub-menu.
    """
    dao = DAO()
    
    if option == 1:
        table_name, dict_register = functions.request_info(menu)
        dao.register(table_name, dict_register)
        if menu == 'servicio':
            vet_name = dao.listTable('veterinary')[1][1]
            cust_table = dao.listTable('customer')
            dict_bill = functions.generate_bill(vet_name, cust_table, dict_register)
            dao.register('bill', dict_bill)
    elif option == 2:
        # Actualizar
        pass
    elif option == 3:
        name_table = functions.nameTable(menu)
        table = dao.listTable(name_table)
        functions.showTable(table)
        delete_id = functions.request_deletion_info(table)
        if not(delete_id == ''):
            dao.delete(name_table, delete_id)
    elif option == 4:
        name_table = functions.nameTable(menu)
        table = dao.listTable(name_table)
        functions.showTable(table)
    else:
        print("Opción no válida...")
   
def display_history():
    dao = DAO()
    table = dao.listTable('historical')
    functions.showTable(table)

def display_bill():
    dao = DAO()
    table = dao.listTable('bill')
    functions.showTable(table)

def display_vet_info():
    dao = DAO()
    table = dao.listTable('veterinary')
    functions.showTable(table)

main_menu() 
