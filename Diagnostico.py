from Proyecto_Veterinaria.Servicio import Servicio


class Diagnostico(Servicio):
    def __init__(self, fecha, precio, duracion, enfermedad, gravedad, MedicoVeterinario, observaciones):
        super().__init__(fecha, precio, duracion)
        self.enfermedad = enfermedad
        self.gravedad = gravedad
        self.MedicoVeterinario = MedicoVeterinario
        self.observacion = observaciones