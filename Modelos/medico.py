from Modelos.persona import Persona


class Medico(Persona):
    # cedula, nombres, apellidos, telefono_contacto,
    def __init__(self, tipo_identificacion, numero_identificacion, nombre, apellido, celular, telefonos, especialidad, direccion):
        super().__init__(tipo_identificacion, numero_identificacion, nombre, apellido, celular, telefonos)
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


