from Proyecto_Veterinaria.Servicio import Servicio

class Cuidados(Servicio):
    def __init__(self, fecha, precio, duracion, tipo_cuidado):
        super().__init__(fecha, precio, duracion)
        self.tipo_cuidado = tipo_cuidado

    def dar_cuidado(self, Mascota):
        if self.tipo_cuidado == 1:
            return "Corte de pelo para la mascota " + Mascota
        elif self.tipo_cuidado == 2:
            return "Baño para la mascota " + Mascota
        elif self.tipo_cuidado == 3:
            return "Vacunacion para la mascota " + Mascota
            
        