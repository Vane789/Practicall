class Orden:
    def __init__(self, consecutivo, fecha_solicitud, fecha_tratante, medico_tratante, numero_orden):
        self._consecutivo = consecutivo
        self._fecha_solicitud = fecha_solicitud
        self._medico_tratante = medico_tratante
        self._numero_orden = numero_orden
        self._fecha_tratante = fecha_tratante

    # Gets y sets
    def set_consecutivo(self, consecutivo):
        self._consecutivo = consecutivo

    def get_consecutivo(self):
        return self._consecutivo
    
    def mostrar_datos(self):
        print(f"Consecutivo: {self._consecutivo}")
        print(f"Fecha de Solicitud: {self._fecha_solicitud}")
        print(f"Médico Tratante: {self._medico_tratante}")
        print(f"Número de Orden: {self._numero_orden}")
        print(f"Fecha de Tratante: {self._fecha_tratante}")

    def set_fecha_solicitud(self, fecha_solicitud):
        self._fecha_solicitud = fecha_solicitud

    def get_fecha_tratante(self):
        return self._fecha_tratante
    
    def set_fecha_tratante(self, fecha_tratante):
        self._fecha_tratante = fecha_tratante

    def get_fecha_solicitud(self):
        return self._fecha_solicitud

    def set_medico_tratante(self, medico_tratante):
        self._medico_tratante = medico_tratante

    def get_medico_tratante(self):
        return self._medico_tratante

    def set_numero_orden(self, numero_orden):
        self._numero_orden = numero_orden

    def get_numero_orden(self):
        return self._numero_orden
    
    def __str__(self):
        return f"Consecutivo: {self._consecutivo}, Fecha Solicitud: {self._fecha_solicitud}, Medico Tratante: {self._medico_tratante}, Numero de Orden: {self._numero_orden}, Fecha Tratante: {self._fecha_tratante}"


    # Funciones
