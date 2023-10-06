from Modelos.medico import Medico
from laboratorio import laboratorio
from Metodos.medicos import *
import datetime


Ordenes = []
consecutivo = 1

def crear_orden(consecutivo, medico):
    paciente = input("Ingrese el nombre del paciente: ")
    numero_orden_medico = input("Ingrese el número de orden del médico: ")

    nueva_orden = {
        "consecutivo": consecutivo,
        "paciente": paciente,
        "medico": medico,
        "fecha_solicitud": datetime.date.today(),
        "fecha_ingreso": datetime.date.today(),
        "numero_orden_medico": numero_orden_medico,
    }

    Ordenes.append(nueva_orden)

    print(f"Datos de la orden{nueva_orden} ")
    print(f"Orden Creada y agregada a la lista de órdenes")






def registrar_medico(cedula):
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



