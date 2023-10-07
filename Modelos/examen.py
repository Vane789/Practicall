class Examen:
    def __init__(self, tipo_de_examen, fecha_cita, fecha_realizacion_examen, observacion, valor):
        self._tipo_de_examen = tipo_de_examen
        self._fecha_cita = fecha_cita
        self._fecha_realizacion_examen = fecha_realizacion_examen
        self._observacion = observacion
        self._valor = valor

    def get_tipo_de_examen(self):
        return self._tipo_de_examen
    
    def mostrar_datos(self):
        print(f"Tipo examen: {self._tipo_de_examen}")
        print(f"Fecha cita: {self._fecha_cita}")
        print(f"Fecha realización del examen: {self._fecha_realizacion_examen}")
        print(f"Observaciones: {self._observacion}")
        print(f"Valor: {self._valor}")

    def set_tipo_de_examen(self, tipo_de_examen):
        self._tipo_de_examen = tipo_de_examen

    def get_fecha_cita(self):
        return self._fecha_cita

    def set_fecha_cita(self, fecha_cita):
        self._fecha_cita = fecha_cita

    def fecha_realizacion_examen(self):
        return self._fecha_realizacion_examen

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
        
    def __str__(self):
        examenes = f"Tipo de Examen: {self._tipo_de_examen}, Fecha de la cita: {self._fecha_cita}, Fecha realización examen: {self._fecha_realizacion_examen}, Observaciones: {self._observacion}, Valor: {self._valor}"
        return examenes
