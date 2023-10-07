from laboratorio import laboratorio
from datetime import datetime
from Metodos.examenes import *

def crear_orden():
    paciente = input("Ingrese el nombre del paciente: ")
    print("""Lista de médicos""")
    for medico in laboratorio.medicos:
        print(f"Nombre: {medico.get_nombre()} Cedula: {medico.get_numero_identificacion()}")
    cedula_medico = input("Ingrese la cédula del médico: ")
    encontrado = False
    nombre_medico = ""
    for medico in laboratorio.medicos:
        if cedula_medico == medico.get_numero_identificacion():
            nombre_medico = medico.get_nombre()
            encontrado = True
            break
    if encontrado:
        numero_orden_medico = input("Ingrese el número de orden del médico: ")
        if numero_orden_medico not in [orden["numero_orden_medico"] for orden in laboratorio.ordenes]:
            date = datetime.now()
            format_date = date.strftime("%Y-%m-%d %H:%M:%S")
            nueva_orden = {
                "consecutivo": len(laboratorio.ordenes)+1,  
                "paciente": paciente,
                "medico": nombre_medico,
                "fecha_solicitud": format_date,
                "fecha_ingreso": format_date,
                "numero_orden_medico": numero_orden_medico,
            }
            laboratorio.ordenes.append(nueva_orden)
            print(f"Datos de la orden{nueva_orden} ")
            print(f"Orden creada y agregada a la lista de órdenes")
            crear_examenes()
        else: 
            print("El número de orden ya existe, debe tener una orden única")
    else:
        print("No existe el médico con esa cédula")