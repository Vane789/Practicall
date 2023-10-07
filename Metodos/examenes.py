from laboratorio import laboratorio
from Modelos.examen import Examen
from datetime import datetime

def crear_examenes():
    print("""
        -------------------------------------------------------
                        [ REGISTRAR EXAMENES ]
        -------------------------------------------------------
        """)
    print("""Lista de examenes""")
    for examen in laboratorio.examenes:
        print(f"Tipo de examen: {examen.get_tipo_de_examen()} Valor: {examen.get_valor()}")
    tipo_examen = input("Ingrese el tipo de examen requerido: ")
    encontrado = False
    valor = ""
    for examen in laboratorio.examenes:
        if tipo_examen == examen.get_tipo_de_examen():
            valor = examen.get_valor()
            encontrado = True
            break
    if encontrado:
        fecha_cita = input("Ingrese la fecha de la cita: ")
        fecha_realizacion_examen = input("Ingrese la fecha de realización del examen: ")
        observacion = input("Ingrese la observacion: ")
        nuevo_examen = {
            "tipo_examen": tipo_examen,
            "fecha_cita": fecha_cita,
            "fecha_realizacion_examen": fecha_realizacion_examen,
            "observacion": observacion,
            "valor": valor,
        }
        laboratorio.examenes.append(nuevo_examen)
        print(f"Datos del examen{nuevo_examen} ")
        print(f"Examen creado y agregada a la lista de examenes")
    else: 
        print("No existe el examen")
