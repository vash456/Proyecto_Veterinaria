from connection import DAO
import functions_1

def main_menu():
    """Display the main menu."""
    continue_main = True
    while continue_main == True:
        right_option_main = False
        while not right_option_main:
            print("============= MENÚ PRINCIPAL =============")
            print("1. Clientes")
            print("2. Mascotas")
            print("3. Veterinarios")
            print("4. Servicios")
            print("5. Historial")
            print("6. Facturas")
            print("7. Ver información veterinaria")
            print("8. Salir")   
            print("==========================================")
            
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
        except:
            print("Ocurrió un error...")
    elif option_main == 2:
        try:
            menu = "mascota"
            sub_menu(menu)
        except:
            print("Ocurrió un error...")  
    elif option_main == 3:
        try:
            menu = "veterinario"
            sub_menu(menu)
        except:
            print("Ocurrió un error...")
    elif option_main == 4:
        try:
            menu = "servicio"
            # Generar factura automáticamente
            sub_menu(menu)            
        except:
            print("Ocurrió un error...")
    elif option_main == 5:
        try:
            display_history()
        except:
            print("Ocurrió un error...")
    elif option_main == 6:
        try:
            display_bill()
        except:
            print("Ocurrió un error...")
    elif option_main == 7:
        try:
            display_vet_info()
        except:
            print("Ocurrió un error...")
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
            print("============= MENÚ {0}S =============".format(menu.upper()))
            print("1. Registrar {0}".format(menu))
            print("2. Actualizar {0}".format(menu))
            print("3. Eliminar {0}".format(menu))
            print("4. Listar {0}s".format(menu))
            print("5. Voler")
            print("==========================================")
            
            option = int(input("Seleccione una opción: "))
        
            if option < 1 or option > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 5:
                continue_menu = False
                main_menu()
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
        table, dict_register = functions_1.request_info(menu)
        dao.register(table, dict_register)
    elif option == 2:
        # Actualizar
        pass
    elif option == 3:
        # Eliminar
        pass
    elif option == 4:
        # Listar
        pass
    else:
        print("Opción no válida...")
       
 
def display_history():
    pass

def display_bill():
    pass

def display_vet_info():
    pass

main_menu() 