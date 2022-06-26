class Mascota:
    def __init__(self, carnet, nombre, especie, raza, edad, color, peso, genero, propietario):
        self._carnet = carnet 
        self._nombre = nombre 
        self._especie = especie 
        self._raza = raza 
        self._edad = edad 
        self._color = color 
        self._peso = peso 
        self._genero = genero 
        self._propietario = propietario
        
    def get_carnet(self):
        return(self._carnet)
    
    def get_nombre(self):
        return(self._nombre)
    
    def get_propietario(self):
        return(self._propietario) 