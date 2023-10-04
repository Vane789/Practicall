class Entidad:
    def __init__(
        self,
        nit,
        telefonos,
        celular,
        correo,
        nombre_del_contacto,
        telefono_del_contacto,
        tipo_entidad,
    ):
        self._nit = nit
        self._telefonos = telefonos
        self._celular = celular
        self._correo = correo
        self._nombre_del_contacto = nombre_del_contacto
        self._telefono_del_contacto = telefono_del_contacto
        self._tipo_entidad = tipo_entidad

    def get_nit(self):
        return self._nit

    def set_nit(self, nit):
        self._nit = nit

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_celular(self):
        return self._celular

    def set_celular(self, celular):
        self._celular = celular

    def get_correo(self):
        return self._correo

    def set_correo(self, correo):
        self._correo = correo

    def get_nombre_del_contacto(self):
        return self._nombre_del_contacto

    def set_nombre_del_contacto(self, nombre_del_contacto):
        self._nombre_del_contacto = nombre_del_contacto

    def get_telefono_del_contacto(self):
        return self._telefono_del_contacto

    def set_telefono_del_contacto(self, telefono_del_contacto):
        self._telefono_del_contacto = telefono_del_contacto

    def get_tipo_entidad(self):
        return self._tipo_entidad

    def set_tipo_entidad(self, tipo_entidad):
        self._tipo_entidad = tipo_entidad
