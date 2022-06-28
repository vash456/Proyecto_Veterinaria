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
    
    # def listTable(self, table):
    #     if self.connection.is_connected():
    #         try:
    #             cursor = self.connection.cursor()
    #             sql = "select * from {0}"
    #             cursor.execute(sql.format(table))
    #             query = cursor.fetchall()
    #             return query
    #         except Error as er:
    #             print("Error al intentar la conexion: {0}".format(er))

    def register(self,table,dict_register):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()

                sql = """INSERT INTO {0} ({1}) VALUES {2};"""
                cursor.execute(sql.format(table, ', '.join(tuple(dict_register.keys())), tuple(dict_register.values())))
                self.connection.commit()
                print("Registro guardado\n")
            except Error as er:
                print("Error al intentar la conexion: {0}".format(er))

    # def update(self,sql,lista):
    #     if self.connection.is_connected():
    #         try:
    #             cursor = self.connection.cursor()
    #             # sql = """UPDATE customer SET name = '{0}', last_name = '{1}', cc = '{2}', age = '{3}', tell = '{4}', email = '{5}' 
    #             # WHERE idCustomer = {6}"""
    #             cursor.execute(sql.format(*lista))
    #             # cursor.execute(sql.format(  customer[0], 
    #             #                             customer[1], 
    #             #                             customer[2], 
    #             #                             customer[3], 
    #             #                             customer[4], 
    #             #                             customer[5],
    #             #                             customer[6]))
    #             cursor.execute(sql.format(*lista))
    #             self.connection.commit()
    #             print("Registro guardado\n")
    #         except Error as er:
    #             print("Error al intentar la conexion: {0}".format(er))
                
    # def search(self,id, table):
    #     if self.connection.is_connected():
    #         try:
    #             cursor = self.connection.cursor()
    #             sql = "select * FROM {0} WHERE id = {1}"
    #             cursor.execute(sql.format(table,id))
    #             self.connection.commit()
    #             print("Registro eliminado\n")
    #         except Error as er:
    #             print("Error al intentar la conexion: {0}".format(er))

    # def delete(self,id, table):
    #     if self.connection.is_connected():
    #         try:
    #             cursor = self.connection.cursor()
    #             sql = "DELETE FROM {0} WHERE id = {1}"
    #             cursor.execute(sql.format(table,id))
    #             self.connection.commit()
    #             print("Registro eliminado\n")
    #         except Error as er:
    #             print("Error al intentar la conexion: {0}".format(er))