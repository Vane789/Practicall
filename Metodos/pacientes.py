from Modelos.paciente import Paciente
from laboratorio import laboratorio
from Metodos.medicos import *


def registrar_examen():
    cedula = input("Cúal es tu cédula: ")
    validar = validarPaciente(cedula)
    #print("validaaar: ", validar)
    if validar:
        nombre = validar["nombre"]
        print(f"Hola de nuevo {nombre}, deseas hoy realizar un examen")
        #print("flujo de crear una orden")
        crear_orden()
    else:
        print("El paciente no existe")
        #print("Flujo para crear un paciente")
        registrar_paciente(cedula)
        
def registrar_paciente(cedula):  
    tipo_identificacion = input("Tipo de identificación (CC, TI): ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    celular = input("Número de celular: ")
    telefonos = input("Teléfonos separados por coma: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    correo = input("Correo electrónico: ")
    nombre_contacto = input("Nombre de contacto de emergencia: ")
    telefono_contacto = input("Teléfono de contacto de emergencia: ")
    POS = input("Tipo de POS (Básico, PAC, Prepagado, Subsidiado): ")
    tipo_paciente = input("Tipo de paciente: ")
    #paciente = Paciente("CC", "12345678", "Vane", "Cardona", "321222333", "6046791", "01-01-1999", "latoxica@gmail.com","miguel", "123", "pos si", "gay")
    paciente = Paciente(tipo_identificacion, cedula, nombre, apellido, celular, telefonos, fecha_nacimiento, correo, nombre_contacto, telefono_contacto, POS, tipo_paciente)
    laboratorio.pacientes.append(paciente)
    print("Paciente agregado con éxito")


def validarPaciente(id):
    for x in laboratorio.pacientes:
        if x.get_numero_identificacion() == id:
            return {
                "respuesta": True,
                "nombre": x.get_nombre()
            }
    return False
    