from persona import Persona


class Paciente(Persona):
    def __init__(
        self,
        tipo_identificacion,
        numero_identificacion,
        nombre,
        apellido,
        fecha_de_nacimiento,
        celular,
        telefonos,
        nombre_contacto,
        telefono_contacto,
        pos,
        tipo_paciente,
    ):
        super().__init__(
            tipo_identificacion,
            numero_identificacion,
            nombre,
            apellido,
            fecha_de_nacimiento,
            celular,
            telefonos,
            nombre_contacto,
            telefono_contacto,
        )
        self._pos = pos
        self._tipo_paciente = tipo_paciente
        self._ordenes_examenes = []


    # Gets y sets
    def set_pos(self, pos):
        self._pos = pos


    def get_pos(self):
        return self._pos


    def set_tipo_paciente(self, tipo_paciente):
        self._tipo_paciente = tipo_paciente


    def get_tipo_paciente(self):
        return self._tipo_paciente


    def set_ordenes_examenes(self, ordenes_examenes):
        self._ordenes_examenes = ordenes_examenes


    def get_ordenes_examenes(self):
        return self._ordenes_examenes


    # Funciones


    def registrar_paciente(identificacion,nombres,apellidos,fecha_nacimiento,telefonos,celular,correo,nombre_contacto,telefono_contacto,pos,tipo_paciente):
        paciente = Paciente(identificacion,nombres,apellidos,fecha_nacimiento,telefonos,celular,correo,nombre_contacto,telefono_contacto,pos,tipo_paciente,
        )
