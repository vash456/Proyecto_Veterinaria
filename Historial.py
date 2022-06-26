class Historial:
    def __init__(self, customer, carnet, nombre_mascota, servicio, fecha, hora, observacion):
        self._customer = customer
        self._carnet = carnet
        self._nombre_mascota = nombre_mascota
        self._servicio = servicio
        self._fecha = fecha 
        self._hora = hora
        self._observacion = observacion
        
    def get_cliente(self):
        return(self._cliente)
        
    def get_nombre_mascota(self):
        return (self._nombre_mascota)
    
    def get_carnet(self):
        return(self._carnet)
    
    def get_fecha(self):
        return(self._fecha)
    
    def __str__(self):
        return ()
    
        
        