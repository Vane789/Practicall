

from Persona import  Persona
class medico(Persona):

    #cedula, nombres, apellidos, telefonoContacto,
    def __init__(self, id, direccion, especialidad, cedula, nombres, apellidos, telefonoContacto):
        super().__init__(id, cedula, nombres, apellidos, telefonoContacto)

        self._direccion = direccion
        self._especialidad = especialidad

    def get_direccion(self):
        return self._direccion
    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad



