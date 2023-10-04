class entidad():
    def __init__(self, nit, telefono, celular, correo, nomConExterno, TelConExterno, tipoEntidad):
        self._nit = nit
        self._telefono = telefono
        self._celular = celular
        self._correo = correo
        self._nomConExterno = nomConExterno
        self._TelConExterno = TelConExterno
        self._tipoEntidad = tipoEntidad

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

    def get_nomConExterno(self):
        return self._nomConExterno
    def set_nomConExterno(self, nomConExterno):
        self._nomConExterno = nomConExterno

    def get_TelConExterno(self):
        return self._TelConExterno
    def set_TelConExterno(self, TelConExterno):
        self._TelConExterno = TelConExterno

    def get_tipoEntidad(self):
        return self._tipoEntidad
    def set_tipoEntidad(self, tipoEntidad):
        self._tipoEntidad = tipoEntidad
