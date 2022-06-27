import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                port  = 3306,
                user = 'root',
                password = '1040',
                db = 'bd_veterinary'
            )
        except Error as er:
            print("Error al intentar la conexion: {0}".format(er))
    
    def listCustomers(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "select * from customer"
                cursor.execute(sql)
                query = cursor.fetchall()
                return query
            except Error as er:
                print("Error al intentar la conexion: {0}".format(er))

    def registerCustomer(self,customer):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = """INSERT INTO customer (name, last_name, cc, age, tell, email) 
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');"""
                cursor.execute(sql.format(  customer[0], 
                                            customer[1], 
                                            customer[2], 
                                            customer[3], 
                                            customer[4], 
                                            customer[5]))
                
                self.connection.commit()
                print("Registro guardado\n")
            except Error as er:
                print("Error al intentar la conexion: {0}".format(er))

    def actualizarCustomer(self,customer):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = """UPDATE customer SET name = '{0}', last_name = '{1}', cc = '{2}', age = '{3}', tell = '{4}', email = '{5}' 
                WHERE idCustomer = {6}"""
                cursor.execute(sql.format(  customer[0], 
                                            customer[1], 
                                            customer[2], 
                                            customer[3], 
                                            customer[4], 
                                            customer[5],
                                            customer[6]))
                
                self.connection.commit()
                print("Registro guardado\n")
            except Error as er:
                print("Error al intentar la conexion: {0}".format(er))

    def eliminarCustomer(self,idCustomer):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM customer WHERE idCustomer = {0}"
                cursor.execute(sql.format(idCustomer))
                self.connection.commit()
                print("Registro eliminado\n")
            except Error as er:
                print("Error al intentar la conexion: {0}".format(er))