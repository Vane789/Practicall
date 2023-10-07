from Modelos.persona import Persona
from Modelos.orden import Orden

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
        direccion
    ):
        super().__init__(
            tipo_identificacion,
            numero_identificacion,
            nombre,
            apellido,
            celular,
            telefonos,
            direccion
        )
        self._fecha_de_nacimiento = fecha_de_nacimiento
        self._correo = correo
        self._nombre_contacto = nombre_contacto
        self._telefono_contacto = telefono_contacto
        self._pos = pos
        self._tipo_paciente = tipo_paciente
        self._ordenes = []
        self._examenes = []


    # Gets y sets
    def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
        self._fecha_de_nacimiento = fecha_de_nacimiento
    
    def get_fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento
    
    def get_ordenes(self):
        return self._ordenes
    
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

    def get_examenes(self):
        return self._examenes
    
    def mostrar_informacion(self):
        atributos = [
            "tipo_identificacion",
            "numero_identificacion",
            "nombre",
            "apellido",
            "celular",
            "telefonos",
            "fecha_de_nacimiento",
            "correo",
            "nombre_contacto",
            "telefono_contacto",
            "pos",
            "tipo_paciente",
            "direccion"
        ]

        informacion = []
        for atributo in atributos: 
            valor = getattr(self, f"_{atributo}")
            informacion.append(f"{atributo}: {valor}")
        return "\n".join(informacion)
        
    def validar(id, pacientes):
        for x in pacientes:
            if x.get_numero_identificacion() == id:
                return {"respuesta": True, "nombre": x.get_nombre()}
        return False 
    
    def __str__(self):
        paciente_info = f"Tipo de Identificación: {self._tipo_identificacion}, Número de Identificación: {self._numero_identificacion}, Nombre: {self._nombre}, Apellido: {self._apellido}, Celular: {self._celular}, Teléfonos: {self._telefonos}, Fecha de Nacimiento: {self._fecha_de_nacimiento}, Correo: {self._correo}, Nombre de Contacto: {self._nombre_contacto}, Teléfono de Contacto: {self._telefono_contacto}, POS: {self._pos}, Tipo de Paciente: {self._tipo_paciente}, Dirección: {self._direccion}"

        ordenes_info = "\nOrdenes:"
        for orden in self._ordenes:
            ordenes_info += f"\n{str(orden)}"
            
        examenes_info = "\nExamenes:"
        for examen in self._examenes:
            examenes_info += f"\n{str(examen)}"

        return paciente_info + ordenes_info + examenes_info

