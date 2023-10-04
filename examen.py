class Examen:
    def __init__(self, tipo_de_examen, fecha_cita, fecha_realizacion_examen, observacion, valor):
        self._tipo_de_examen = tipo_de_examen
        self._fecha_cita = fecha_cita
        self._fecha_realizacion_examen = fecha_realizacion_examen
        self._observacion = observacion
        self._valor = valor

    def get_tipo_de_examen(self):
        return self._tipo_de_examen

    def set_tipo_de_examen(self, tipo_de_examen):
        self._tipo_de_examen = tipo_de_examen

    def get_fecha_cita(self):
        return self._fecha_cita

    def set_fecha_cita(self, fecha_cita):
        self._fecha_cita = fecha_cita

    @property
    def fecha_realizacion_examen(self):
        return self._fecha_realizacion_examen

    @fecha_realizacion_examen.setter
    def fecha_realizacion_examen(self, valor):
        self._fecha_realizacion_examen = valor 

    def get_observacion(self):
        return self._observacion

    def set_observacion(self, observacion):
        self._observacion = observacion

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor