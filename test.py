import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                port  = 3306,
                user = 'root',
                password = 'Grifo-99',
                db = 'db_veterinaria'
            )
        except Error as er:
            print(f"Error al intentar la conexion: {0}".format(er))
            
    def register(self,table,dict):
            if self.connection.is_connected():
                try:
                    cursor = self.connection.cursor()

                    sql = """INSERT INTO {0} ({1}) VALUES {2};"""
                    cursor.execute(sql.format(table, ', '.join(tuple(dict.keys())), tuple(dict.values())))
                    self.connection.commit()
                    print("Registro guardado\n")
                except Error as er:
                    print("Error al intentar la conexion: {0}".format(er))

table = 'pets'

name = 'Lola'
species = 'Perro'
age = '2'
race = 'Pug'
color = 'Gris'
weight = '8'
gender = 'Femenino'
owner = 1

pet = {'name':name, 'species':species, 'age':age, 'race':race, 'color':color, 'weight':weight,
        'gender':gender, 'customer_idCustomer':owner}
dict_register = pet
dao =DAO()
dao.register(table, dict_register)