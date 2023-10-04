class Persona ():
        def __init__(self,tipo_identificacion, numero_identificacion, nombre, apellido,fecha_de_nacimiento, celular, telefonos, nombre_contacto, telefono_contacto):
        
                self._tipo_identificacion = tipo_identificacion
                self._numero_identificacion = numero_identificacion
                self._nombre = nombre
                self._apellido = apellido
                self._fecha_de_nacimiento = fecha_de_nacimiento
                self._celular = celular
                self._telefonos = telefonos
                self._nombre_contacto = nombre_contacto
                self._telefono_contacto = telefono_contacto


        # Gets   

        def get_tipo_identificacion(self):
                return self._tipo_identificacion

        def get_numero_identificacion(self):
                return self._numero_identificacion

        def get_nombre(self):
                return self._nombre

        def get_apellido(self):
                return self._apellido

        def get_fecha_de_nacimiento(self):
                return self._fecha_de_nacimiento

        def get_celular(self):
                return self._celular

        def get_telefonos(self):
                return self._telefonos

        def get_nombre_contacto(self):
                return self._nombre_contacto

        def get_telefono_contacto(self):
                return self._telefono_contacto

        #Sets

        def set_tipo_identificacion(self, tipo_identificacion):
                self._tipo_identificacion = tipo_identificacion

        def set_numero_identificacion(self, numero_identificacion):
                self._numero_identificacion = numero_identificacion

        def set_nombre(self, nombre):
                self._nombre = nombre

        def set_apellido(self, apellido):
                self._apellido = apellido

        def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
                self._fecha_de_nacimiento = fecha_de_nacimiento

        def set_celular(self, celular):
                self._celular = celular

        def set_telefonos(self, telefonos):
                self._telefonos = telefonos

        def set_nombre_contacto(self, nombre_contacto):
                self._nombre_contacto = nombre_contacto

        def set_telefono_contacto(self, telefono_contacto):
                self._telefono_contacto = telefono_contacto

