class Factura:
    def __init__(self, fecha, cliente, servicio, precio):
        self._fecha = fecha
        self._cliente = cliente
        self._servicio = servicio
        self._precio = precio
        
    def imprimir_factura(self):
        print(f'''
              fecha: {self._fecha}
              nombre: {self._cliente}
              servicio prestado: {self._servicio}
              
              Total: {self._precio}
              ''')
        
    # def pagar_factura(self, dinero):
    #     if self._precio != dinero:
    #         print("La cantidad no es correcta") 
    #     else:
    #         print("Pago exitoso")
            