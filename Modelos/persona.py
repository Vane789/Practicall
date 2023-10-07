#Abstracción se aplica creando Persona  creación de una clase base o genérica que contiene atributos 
# y métodos comunes que se comparten entre varias clases derivadas o subclases. 
class Persona ():
        def __init__(self,tipo_identificacion, numero_identificacion, nombre, apellido, celular, telefonos, direccion):
        
                self._tipo_identificacion = tipo_identificacion
                self._numero_identificacion = numero_identificacion
                self._nombre = nombre
                self._apellido = apellido
                self._celular = celular
                self._telefonos = telefonos
                self.direccion = direccion

        # Gets   

        def get_tipo_identificacion(self):
                return self._tipo_identificacion

        def get_numero_identificacion(self):
                return self._numero_identificacion

        def get_nombre(self):
                return self._nombre

        def get_apellido(self):
                return self._apellido

        def get_celular(self):
                return self._celular

        def get_telefonos(self):
                return self._telefonos
        
        def get_direccion(self):
                return self._direccion
        #Sets

        def set_tipo_identificacion(self, tipo_identificacion):
                self._tipo_identificacion = tipo_identificacion

        def set_numero_identificacion(self, numero_identificacion):
                self._numero_identificacion = numero_identificacion

        def set_nombre(self, nombre):
                self._nombre = nombre

        def set_apellido(self, apellido):
                self._apellido = apellido

        def set_celular(self, celular):
                self._celular = celular

        def set_telefonos(self, telefonos):
                self._telefonos = telefonos
        
        def set_direccion(self, direccion):
                self._direccion = direccion


        # def validar_informacion():
        #         print("No se puede validar la información de una persona genérica")