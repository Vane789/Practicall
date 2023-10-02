class examen():
    def __init__(self, id, tipoExamen, fechaCita, fechaRealizacion, Observaciones):
        self._id = id
        self._tipoExamen = tipoExamen
        self._fechaCita = fechaCita
        self._fechaRealizacion = fechaRealizacion
        self._Observaciones = Observaciones

    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id

    def get_tipoExamen(self):
        return self._tipoExamen
    def set_tipoExamen(self, tipoExamen):
        self._tipoExamen = tipoExamen

    def get_fechaCita(self):
        return self._fechaCita
    def set_fechaCita(self, fechaCita):
        self._fechaCita = fechaCita

    def get_fechaRealizacion(self):
        return self._fechaRealizacion

    def set_fechaRealizacion(self, fechaRealizacion):
        self._fechaRealizacion= fechaRealizacion

    def get_Observaciones(self):
        return self._Observaciones

    def set_Observaciones(self, Observaciones):
        self._Observaciones= Observaciones


