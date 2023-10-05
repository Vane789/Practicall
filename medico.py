from persona import Persona


class Medico(Persona):
    # cedula, nombres, apellidos, telefonoContacto,
    def __init__(self, cedula, nombres, apellidos, telefonoContacto, especialidad, direccion):
        super().__init__(cedula, nombres, apellidos, telefonoContacto)
        self._especialidad = especialidad
        self._direccion = direccion

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion
