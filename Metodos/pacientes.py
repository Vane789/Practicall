from Modelos.paciente import Paciente
from laboratorio import laboratorio
from Metodos.medicos import *
from Metodos.ordenes import *

def validar_informacion(cedula = None):
    if cedula == None:
        cedula = input("Cúal es la cédula del paciente: ")
    validar_paciente = validar(cedula)
    if validar_paciente:
        nombre = validar_paciente["nombre"]
        print(f"Hola {nombre}, deseas realizar un examen")
        crear_orden(validar_paciente["ordenes"], validar_paciente["examenes"])
    else:
        print("El paciente no existe")
        registrar_paciente(cedula)
        print("Deseas registar una orden")
        if input("Si o cualquiero otro caracter: ") == ("Si").lower():
            validar_informacion(cedula)
        else:
            print("Salir de la creación de orden")
        
def registrar_paciente(cedula):
    print("""
        -------------------------------------------------------
                        [ REGISTRAR PACIENTE ]
        -------------------------------------------------------
        """)
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
    direccion = input("Direccion: ")
    paciente = Paciente(tipo_identificacion, cedula, nombre, apellido, celular, telefonos, fecha_nacimiento, correo, nombre_contacto, telefono_contacto, POS, tipo_paciente, direccion)
    laboratorio.pacientes.append(paciente)
    print("Paciente agregado con éxito")

def ver_todos_pacientes():
    print("---" * 20)
    for paciente in laboratorio.pacientes:
        print(paciente.mostrar_informacion())
        print("---" * 20)

def ver_ordenes_paciente():
    print("---" * 20)
    existe = False
    cedula_paciente = input("Cédula del paciente: ")

    for paciente in laboratorio.pacientes:
        if cedula_paciente == paciente.get_numero_identificacion():
            existe = True
            paciente
            break  

    if existe:
        for orden in paciente.get_ordenes():
                print("orden ", orden)
    else:
        print(f"El paciente con la cédula {cedula_paciente} no tiene órdenes.")


def validar(id):
    for i, dato in enumerate(laboratorio.pacientes):
        print(dato)
        if dato.get_numero_identificacion() == id:
            return {
                "respuesta": True,
                "nombre": dato.get_nombre(),
                "ordenes": dato.get_ordenes(),
                "examenes": dato.get_examenes()
            }
    return False
    