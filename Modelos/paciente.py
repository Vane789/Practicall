from Modelos.persona import Persona


class Paciente(Persona):
    def __init__(
        self,
        tipo_identificacion, 
        numero_identificacion, 
        nombre, 
        apellido, 
        celular, 
        telefonos,
        fecha_de_nacimiento,
        correo,
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
            celular,
            telefonos,
        )
        self._fecha_de_nacimiento = fecha_de_nacimiento
        self._correo = correo
        self._nombre_contacto = nombre_contacto
        self._telefono_contacto = telefono_contacto
        self._pos = pos
        self._tipo_paciente = tipo_paciente
        self._ordenes_examenes = []


    # Gets y sets
    def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
        self._fecha_de_nacimiento = fecha_de_nacimiento
    
    def get_fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento
    
    def set_correo(self, correo):
        self._correo = correo
        
    def get_correo(self):
        return self._correo
    
    def set_nombre_contacto(self, nombre_contacto):
        self._nombre_contacto = nombre_contacto
        
    def get_nombre_contacto(self):
        return self._nombre_contacto
    
    def set_telefono_contacto(self, telefono_contacto):
        self._telefono_contacto = telefono_contacto
    
    def get_telefono_contacto(self):
        return self._telefono_contacto
    
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

