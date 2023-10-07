from laboratorio import laboratorio
from datetime import datetime
from Metodos.examenes import *
from Modelos.orden import Orden

def crear_orden(ordenes, examenes):
    print("""Lista de médicos""")
    for medico in laboratorio.medicos:
        print(f"Nombre: {medico.get_nombre()} Cédula: {medico.get_numero_identificacion()}")
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
        if numero_orden_medico not in [orden.get_numero_orden() for orden in ordenes]:
            date = datetime.now()
            format_date = date.strftime("%Y-%m-%d %H:%M:%S")
            nueva_orden = Orden(
                len(ordenes)+1,
                nombre_medico,
                format_date,
                format_date,
                numero_orden_medico,
            )   
            ordenes.append(nueva_orden)
            print("---" * 20)
            print("Orden creada con los siguientes datos:")
            ordenes[len(ordenes) -1].mostrar_datos()
            print("---" * 20)
            crear_examenes(examenes)
        else: 
            print("El número de orden ya existe, debe tener una orden única")
    else:
        print("No existe el médico con esa cédula")