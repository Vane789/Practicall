from Modelos.medico import Medico
from laboratorio import laboratorio
from Metodos.medicos import *
from Metodos.ordenes import *

def validar_medico():
        cedula = input("Cúal es tu cédula: ")
        validar_medico = validar(cedula)
        if validar_medico:
            print(f"El medico ya existe con cedula: {cedula}")
        else:
            print("El medico no existe")
            
            #print("Flujo para registrar un medico")
            registrar_medico(cedula)
        
def registrar_medico(cedula):
    print("""
        -------------------------------------------------------
                        [ REGISTRAR MEDICO ]
        -------------------------------------------------------
        """)
    tipo_identificacion = input("Tipo de identificación (CC, CE): ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    celular = input("Número de celular: ")
    telefonos = input("Teléfonos separados por coma: ")
    especialidad = input("Especialidad: ")
    direccion = input("Direccions: ")
    medico = Medico(tipo_identificacion, cedula, nombre, apellido, celular, telefonos, especialidad, direccion )
    laboratorio.medicos.append(medico)
    print("Medico agregado con éxito")



def validar(id):
    for x in laboratorio.medicos:
        if x.get_numero_identificacion() == id:
            return {
                "respuesta": True,
                "nombre": x.get_nombre()
            }
    return False

