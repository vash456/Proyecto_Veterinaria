import mysql.connector
from mysql.connector import Error
from tomlkit import table


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
            print(f"Error al intentar la conexion (connection): {0}".format(er))
    
    #Crear registro dentro de cualquier tabla pasando nombre de tabla, con data en un diccionario   
    def register(self, table_name, dict_register):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = """INSERT INTO {0} ({1}) VALUES {2};"""
                cursor.execute(sql.format(table_name, ', '.join(tuple(dict_register.keys())), tuple(dict_register.values())))               
                self.connection.commit()
                if table_name == 'bill':
                    print("Factura generada\n")
                else:
                    print("Registro guardado\n")
            except Error as er:
                print("Error al intentar la conexion (register): {0}".format(er))
                
    #Listar todos los datos de una tabla
    def listTable(self, name_table):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "select * from {0}"
                cursor.execute(sql.format(name_table))
                query = cursor.fetchall()
                query = list(query)
                query.insert(0, list(cursor.column_names))
                query = tuple(query)
                return query
            except Error as er:
                print("Error al intentar la conexion(listTable): {0}".format(er))

    #Actualizar el registro de una tabla 
    def update(self, table_name, dict_update, id):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                SET = 'SET '
                for k,v in dict_update.items():
                    curr_v = f"'{v}'" if type(v) == str else v
                    SET += "{0} = {1}, ".format(k, curr_v)
                SET = SET[:-2] # Remove the last ","
                sql = """UPDATE {0} {1} WHERE id = {2};"""
                cursor.execute(sql.format(table_name, SET, id))               
                self.connection.commit()
                print("Actualización exitosa\n")
            except Error as er:
                print("Error al intentar la conexion(Update): {0}".format(er))
                
    #Eliminar el registro de alguna tabla
    def delete(self, name_table:str, id:int):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM {0} WHERE id = {1}"
                cursor.execute(sql.format(name_table, id))
                self.connection.commit()
                print("Registro eliminado\n")
            except Error as er:
                print("Error al intentar la conexion(delete): {0}".format(er))