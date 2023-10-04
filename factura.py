class Factura:
    def __init__(self, numero_factura, valor_a_pagar, paciente, fecha_realizacion):
        self._numero_factura = numero_factura
        self._valor_a_pagar = valor_a_pagar
        self._paciente = paciente
        self._fecha_realizacion = fecha_realizacion  

#Gets y sets
 
def set_numero_factura(self, numero_factura):
    self._numero_factura = numero_factura

def get_numero_factura(self):
    return self._numero_factura

def set_valor_a_pagar(self, valor_a_pagar):
    self._valor_a_pagar = valor_a_pagar

def get_valor_a_pagar(self):
    return self._valor_a_pagar

def set_paciente(self, paciente):
    self._paciente = paciente

def get_paciente(self):
    return self._paciente

@property
def fecha_realizacion_factura(self):
    # Lógica para obtener la fecha de realización específica de la factura
    return self._fecha_realizacion_factura

@fecha_realizacion_factura.setter
def fecha_realizacion_factura(self, valor):
    # Lógica para validar o transformar la fecha de realización de la factura
    self._fecha_realizacion_factura = valor

#Funciones

